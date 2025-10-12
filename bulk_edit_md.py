#!/usr/bin/env python3
"""
Bulk edit markdown files in docs/SetupGuide/Controllers/
Performs the following edits:
1. Add empty line before bullet lists (- items)
2. Add empty line before numbered lists (1. 2. etc)
3. Add empty line before tables (| ...)
4. Convert plain-text http links to hyperlink elements
"""

import os
import re
from pathlib import Path


def process_markdown_file(filepath):
    """Process a single markdown file with all edits."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        return False

    modified = False
    new_lines = []
    i = 0

    while i < len(lines):
        current_line = lines[i]

        # Check if we need to add an empty line before this line
        if i > 0:
            prev_line = lines[i - 1]
            prev_line_stripped = prev_line.strip()
            current_line_stripped = current_line.strip()

            # Skip if previous line is already empty
            if prev_line_stripped != '':
                needs_empty_line = False

                # Edit 1: Check for bullet list (- item)
                if re.match(r'^\s*-\s+', current_line):
                    # Check if previous line was also a bullet list item
                    if not re.match(r'^\s*-\s+', prev_line):
                        needs_empty_line = True

                # Edit 2: Check for numbered list (1. item)
                elif re.match(r'^\s*\d+\.\s+', current_line):
                    # Check if previous line was also a numbered list item
                    if not re.match(r'^\s*\d+\.\s+', prev_line):
                        needs_empty_line = True

                # Edit 3: Check for table row (| ...)
                elif re.match(r'^\s*\|', current_line):
                    # Check if previous line was also a table row
                    if not re.match(r'^\s*\|', prev_line):
                        needs_empty_line = True

                if needs_empty_line:
                    new_lines.append('\n')
                    modified = True

        # Edit 4: Convert plain-text http/https links to hyperlink elements
        # Match URLs that are not already in markdown link format
        def replace_plain_links(line):
            # Pattern: find http(s):// URLs that are not part of [text](url) or ![alt](url)
            # Negative lookbehind for ]( to avoid matching URLs already in markdown links
            # Also avoid matching if the URL is followed by ) and preceded by matching [url](
            pattern = r'(?<!\]\()(?<!\[)(https?://[^\s\)]+)(?!\))'

            def replacer(match):
                url = match.group(1)
                # Skip Discord links (discordapp)
                if 'discordapp' in url:
                    return url  # Return unchanged for Discord links
                # Double-check: if the URL appears in the pattern [url](url), don't replace
                # Look for the pattern [<url>](<url>) in the line
                check_pattern = re.escape(f'[{url}]({url})')
                if re.search(check_pattern, line):
                    return url  # Return unchanged if already in proper format
                return f'[{url}]({url})'

            new_line = re.sub(pattern, replacer, line)
            return new_line

        original_line = current_line
        current_line = replace_plain_links(current_line)
        if current_line != original_line:
            modified = True

        new_lines.append(current_line)
        i += 1

    # Write back if modified
    if modified:
        with open(filepath, 'w', encoding='utf-8', newline='\r\n') as f:
            f.writelines(new_lines)
        return True

    return False


def main():
    """Process all markdown files in docs/Programs/"""
    target_dir = Path('docs/')

    if not target_dir.exists():
        print(f"Error: Directory {target_dir} does not exist")
        return

    # Find all .md files recursively
    md_files = list(target_dir.glob('**/*.md'))

    if not md_files:
        print(f"No markdown files found in {target_dir}")
        return

    print(f"Found {len(md_files)} markdown file(s) in {target_dir}")
    print()

    modified_count = 0
    for md_file in md_files:
        print(f"Processing: {md_file.name}...", end=' ')
        if process_markdown_file(md_file):
            print("✓ Modified")
            modified_count += 1
        else:
            print("- No changes needed")

    print()
    print(f"Done! Modified {modified_count} file(s)")


if __name__ == '__main__':
    main()
