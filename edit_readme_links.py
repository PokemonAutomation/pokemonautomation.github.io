#!/usr/bin/env python3
"""
Script to find and modify README.md links in markdown files.
Searches docs/SetupGuide/Controllers/ directory.
Modifies links that start with "../README.md" to "../index.md".
"""

import os
import re
from pathlib import Path


def fix_readme_links(root_dir, dry_run=True):
    """
    Fix README.md links in markdown files by changing "../README.md" to "../index.md".

    Args:
        root_dir: Root directory to search (docs/SetupGuide/Controllers/)
        dry_run: If True, only report changes without modifying files

    Returns:
        Dictionary with statistics about changes made
    """
    stats = {
        'files_modified': 0,
        'links_changed': 0,
        'changes': []
    }

    # Walk through all subdirectories
    for md_file in Path(root_dir).rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8', newline='') as f:
                content = f.read()
                original_content = content

            file_changes = []

            # Replace Markdown links [text](../README.md...) to [text](../index.md...)
            def replace_md_link(match):
                full_match = match.group(0)
                link_text = match.group(1)
                link_path = match.group(2)

                # Only modify paths that start with "../README.md"
                if link_path.startswith('../README.md'):
                    # Replace README.md with index.md
                    new_path = link_path.replace('../README.md', '../index.md', 1)
                    new_match = f'[{link_text}]({new_path})'
                    file_changes.append((link_path, new_path))
                    return new_match

                return full_match

            # Replace HTML links <a href="../README.md...">
            def replace_html_link(match):
                full_tag = match.group(0)
                link_path = match.group(1)

                # Only modify paths that start with "../README.md"
                if link_path.startswith('../README.md'):
                    # Replace README.md with index.md
                    new_path = link_path.replace('../README.md', '../index.md', 1)
                    new_tag = full_tag.replace(f'"{link_path}"', f'"{new_path}"').replace(f"'{link_path}'", f"'{new_path}'")
                    file_changes.append((link_path, new_path))
                    return new_tag

                return full_tag

            # Apply replacements
            # Match markdown links: [text](url)
            content = re.sub(r'\[([^\]]*)\]\(([^)]+)\)', replace_md_link, content)
            # Match HTML anchor tags: <a href="...">
            content = re.sub(r'<a\s+[^>]*href\s*=\s*["\']([^"\']+)["\'][^>]*>', replace_html_link, content)

            # Check if content changed
            if content != original_content and file_changes:
                stats['files_modified'] += 1
                stats['links_changed'] += len(file_changes)
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
    Print the results of the link fixing.

    Args:
        stats: Dictionary from fix_readme_links()
        dry_run: Whether this was a dry run
    """
    if stats['links_changed'] == 0:
        print("No README.md links need to be modified.")
        return

    mode = "Would modify" if dry_run else "Modified"
    print(f"\n{mode} {stats['links_changed']} link(s) in {stats['files_modified']} file(s)\n")
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

    print(f"Processing README.md links in: {docs_controllers_dir}")

    if dry_run:
        print(f"Mode: DRY RUN (use --apply to actually modify files)\n")
    else:
        print(f"Mode: APPLYING CHANGES\n")

    stats = fix_readme_links(docs_controllers_dir, dry_run=dry_run)
    print_results(stats, dry_run=dry_run)

    if dry_run and stats['links_changed'] > 0:
        print("\nTo apply these changes, run: python3 edit_readme_links.py --apply")


if __name__ == "__main__":
    main()
