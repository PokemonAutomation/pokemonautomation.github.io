#!/usr/bin/env python3
"""
Script to revert image path modifications in markdown files.
Searches docs/ directory (excluding index.md files).
Modifies image paths that start with "../../" to remove one "../" prefix.
This reverts the changes made for use_directory_urls: true back to use_directory_urls: false.
"""

import os
import re
from pathlib import Path


def find_image_paths(root_dir):
    """
    Find all image paths in markdown files.

    Args:
        root_dir: Root directory to search (docs/)

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
        # Skip index.md files
        if md_file.name == 'index.md':
            continue

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


def revert_image_paths(root_dir, dry_run=True):
    """
    Revert image paths in markdown files by removing one "../" prefix from paths starting with "../".

    Args:
        root_dir: Root directory to search (docs/)
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

            # Replace HTML img tags with src="../../..." to src="../..."
            def replace_html_img(match):
                full_tag = match.group(0)
                img_path = match.group(1)

                # Skip Discord API images and absolute/http URLs
                if 'discordapp' in img_path.lower() or img_path.startswith(('http://', 'https://', '/')):
                    return full_tag

                # Only modify paths that start with "../"
                if img_path.startswith('../'):
                    # Remove one "../" prefix
                    new_path = img_path[3:]  # Remove first 3 characters "../"
                    new_tag = full_tag.replace(f'"{img_path}"', f'"{new_path}"').replace(f"'{img_path}'", f"'{new_path}'")
                    file_changes.append((img_path, new_path))
                    return new_tag

                return full_tag

            # Replace Markdown images ![alt](../../...) to ![alt](../...)
            def replace_md_img(match):
                full_match = match.group(0)
                alt_text = match.group(1)
                img_path = match.group(2)

                # Skip Discord API images and absolute/http URLs
                if 'discordapp' in img_path.lower() or img_path.startswith(('http://', 'https://', '/')):
                    return full_match

                # Only modify paths that start with "../"
                if img_path.startswith('../'):
                    # Remove one "../" prefix
                    new_path = img_path[3:]  # Remove first 3 characters "../"
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
    Print the results of the image path reverting.

    Args:
        stats: Dictionary from revert_image_paths()
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
    docs_dir = script_dir / "docs"

    if not docs_dir.exists():
        print(f"Error: Directory not found: {docs_dir}")
        return

    # Check if --apply flag is provided
    dry_run = '--apply' not in sys.argv

    print(f"Processing image paths in: {docs_dir}")
    print(f"Excluding: index.md files and Discord API images")

    if dry_run:
        print(f"Mode: DRY RUN (use --apply to actually modify files)\n")
    else:
        print(f"Mode: APPLYING CHANGES\n")

    stats = revert_image_paths(docs_dir, dry_run=dry_run)
    print_results(stats, dry_run=dry_run)

    if dry_run and stats['paths_changed'] > 0:
        print("\nTo apply these changes, run: python3 revert_image_paths.py --apply")


if __name__ == "__main__":
    main()
