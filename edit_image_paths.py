#!/usr/bin/env python3
"""
Script to find and modify image paths in markdown files.
Searches docs/SetupGuide/Controllers/ directory (excluding index.md).
Modifies image paths that start with "../Images/" to "../../Images/".
"""

import os
import re
from pathlib import Path


def find_image_paths(root_dir):
    """
    Find all image paths in markdown files.

    Args:
        root_dir: Root directory to search (docs/SetupGuide/Controllers/)

    Returns:
        Dictionary mapping file paths to list of (line_number, line_content, image_path) tuples
    """
    results = {}

    # Pattern to match:
    # 1. HTML img tags: <img src="...">
    # 2. Markdown images: ![alt](path)
    # We'll capture both local and remote URLs
    img_patterns = [
        r'<img\s+[^>]*src\s*=\s*["\']([^"\']+)["\'][^>]*>',  # HTML img tags
        r'!\[([^\]]*)\]\(([^)]+)\)',  # Markdown image syntax
    ]

    combined_pattern = '|'.join(f'({p})' for p in img_patterns)

    # Walk through all subdirectories
    for md_file in Path(root_dir).rglob('*.md'):
        file_results = []

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    # Check for HTML img tags
                    html_matches = re.finditer(r'<img\s+[^>]*src\s*=\s*["\']([^"\']+)["\'][^>]*>', line)
                    for match in html_matches:
                        img_path = match.group(1)
                        # Skip Discord API images
                        if 'discordapp' not in img_path.lower():
                            file_results.append((line_num, line.rstrip(), img_path))

                    # Check for Markdown image syntax
                    md_matches = re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', line)
                    for match in md_matches:
                        img_path = match.group(2)
                        # Skip Discord API images
                        if 'discordapp' not in img_path.lower():
                            file_results.append((line_num, line.rstrip(), img_path))

        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue

        if file_results:
            results[str(md_file)] = file_results

    return results


def fix_image_paths(root_dir, dry_run=True):
    """
    Fix image paths in markdown files by changing "../Images/" to "../../Images/".

    Args:
        root_dir: Root directory to search (docs/SetupGuide/Controllers/)
        dry_run: If True, only report changes without modifying files

    Returns:
        Dictionary with statistics about changes made
    """
    stats = {
        'files_modified': 0,
        'paths_changed': 0,
        'changes': []
    }

    # Walk through all subdirectories
    for md_file in Path(root_dir).rglob('*.md'):
        # Skip index.md files
        if md_file.name == 'index.md':
            continue

        try:
            with open(md_file, 'r', encoding='utf-8', newline='') as f:
                content = f.read()
                original_content = content

            file_changes = []

            # Replace HTML img tags with src="../Images/..." to src="../../Images/..."
            def replace_html_img(match):
                full_tag = match.group(0)
                img_path = match.group(1)

                # Skip Discord API images
                if 'discordapp' in img_path.lower():
                    return full_tag

                # Only modify paths that start with "../Images/"
                if img_path.startswith('../Images/'):
                    new_path = '../' + img_path  # Adds one more "../" by prepending "."
                    new_tag = full_tag.replace(f'"{img_path}"', f'"{new_path}"')
                    file_changes.append((img_path, new_path))
                    return new_tag

                return full_tag

            # Replace Markdown images ![alt](../Images/...) to ![alt](../../Images/...)
            def replace_md_img(match):
                full_match = match.group(0)
                alt_text = match.group(1)
                img_path = match.group(2)

                # Skip Discord API images
                if 'discordapp' in img_path.lower():
                    return full_match

                # Only modify paths that start with "../Images/"
                if img_path.startswith('../Images/'):
                    new_path = '../' + img_path  # Adds one more "../" by prepending "."
                    new_match = f'![{alt_text}]({new_path})'
                    file_changes.append((img_path, new_path))
                    return new_match

                return full_match

            # Apply replacements
            content = re.sub(r'<img\s+[^>]*src\s*=\s*["\']([^"\']+)["\'][^>]*>', replace_html_img, content)
            content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_md_img, content)

            # Check if content changed
            if content != original_content and file_changes:
                stats['files_modified'] += 1
                stats['paths_changed'] += len(file_changes)
                stats['changes'].append({
                    'file': str(md_file),
                    'changes': file_changes
                })

                if not dry_run:
                    # Write the modified content back with Windows line endings (CRLF)
                    # Convert LF to CRLF if needed
                    content_with_crlf = content.replace('\r\n', '\n').replace('\n', '\r\n')
                    with open(md_file, 'w', encoding='utf-8', newline='') as f:
                        f.write(content_with_crlf)

        except Exception as e:
            print(f"Error processing {md_file}: {e}")
            continue

    return stats


def print_results(stats, dry_run=True):
    """
    Print the results of the image path fixing.

    Args:
        stats: Dictionary from fix_image_paths()
        dry_run: Whether this was a dry run
    """
    if stats['paths_changed'] == 0:
        print("No image paths need to be modified.")
        return

    mode = "Would modify" if dry_run else "Modified"
    print(f"\n{mode} {stats['paths_changed']} image path(s) in {stats['files_modified']} file(s)\n")
    print("=" * 80)

    for change_info in stats['changes']:
        print(f"\nFile: {change_info['file']}")
        print("-" * 80)
        for old_path, new_path in change_info['changes']:
            print(f"  {old_path} -> {new_path}")
        print()


def main():
    import sys

    # Get the script directory
    script_dir = Path(__file__).parent
    docs_controllers_dir = script_dir / "docs" / "SetupGuide" / "Controllers"

    if not docs_controllers_dir.exists():
        print(f"Error: Directory not found: {docs_controllers_dir}")
        return

    # Check if --apply flag is provided
    dry_run = '--apply' not in sys.argv

    print(f"Processing image paths in: {docs_controllers_dir}")
    print(f"Excluding: index.md files and Discord API images")

    if dry_run:
        print(f"Mode: DRY RUN (use --apply to actually modify files)\n")
    else:
        print(f"Mode: APPLYING CHANGES\n")

    stats = fix_image_paths(docs_controllers_dir, dry_run=dry_run)
    print_results(stats, dry_run=dry_run)

    if dry_run and stats['paths_changed'] > 0:
        print("\nTo apply these changes, run: python3 edit_image_paths.py --apply")


if __name__ == "__main__":
    main()
