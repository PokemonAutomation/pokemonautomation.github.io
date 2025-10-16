#!/usr/bin/env python3
"""
Find and fix occurrences of an image tag after numbered lines in markdown files.
Searches for patterns like:
1. do something...
    <img src="...">

or

2. do something...

![image](...)

3. plug the cable...

With --apply flag, adds 4-space indentation and proper empty lines around images.
Skips images that are inside table cells or are already properly indented.
"""

import argparse
import os
import re
from pathlib import Path


def is_in_table_cell(lines, line_index):
    """
    Check if a line is inside a table cell by looking for pipe characters.
    A line is in a table if it or nearby lines contain markdown table syntax.

    Args:
        lines: List of all lines in the file
        line_index: Index of the line to check

    Returns:
        True if the line appears to be in a table cell, False otherwise
    """
    current_line = lines[line_index].strip()

    # Check if current line has table pipe characters
    if '|' in current_line:
        return True

    # Check a few lines above and below for table context
    check_range = 3
    start = max(0, line_index - check_range)
    end = min(len(lines), line_index + check_range + 1)

    for i in range(start, end):
        line = lines[i].strip()
        # Look for table separator lines like |---|---|
        if re.match(r'^\|?[\s\-:|]+\|[\s\-:|]*\|', line):
            return True
        # Look for lines with multiple pipes (likely table rows)
        if line.count('|') >= 2:
            return True

    return False


def find_and_fix_patterns(docs_dir='docs', apply_fixes=False):
    """
    Search for image tags after numbered lines in markdown files.
    Optionally fix them by adding 4-space indentation and proper empty lines.
    Skips images that are inside table cells or already properly indented.

    Args:
        docs_dir: Directory to search (default: 'docs')
        apply_fixes: If True, apply fixes and save files

    Returns:
        List of tuples: (file_path, line_number, prev_numbered, image_line, next_numbered,
                        empty_before_count, empty_after_count, needs_indent)
    """
    results = []
    files_to_update = {}  # file_path -> modified_lines

    # Pattern for markdown image: ![...](...) or <img ...>
    image_pattern = re.compile(r'!\[.*?\]\(.*?\)|<img\s+.*?>')

    # Pattern for numbered line: starts with number followed by dot and space
    numbered_pattern = re.compile(r'^\s*\d+\.\s+')

    # Pattern to check if line starts with exactly 4 spaces (already properly indented)
    four_space_pattern = re.compile(r'^    ')

    # Find all .md files in docs directory
    docs_path = Path(docs_dir)
    if not docs_path.exists():
        print(f"Error: Directory '{docs_dir}' does not exist")
        return results

    md_files = list(docs_path.rglob('*.md'))
    print(f"Searching {len(md_files)} markdown files in '{docs_dir}'...\n")

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            modified_lines = lines.copy()
            modifications = []  # List of (line_index, action, value) tuples

            # Check each line for image tag
            for i in range(len(lines)):
                current_line = lines[i].rstrip()

                # Check if current line has an image tag
                if image_pattern.search(current_line):
                    # Skip if this image is in a table cell
                    if is_in_table_cell(lines, i):
                        continue

                    # Check if already properly indented (starts with 4 spaces)
                    already_indented = four_space_pattern.match(lines[i])

                    # Look backward for numbered line (skip empty lines)
                    prev_numbered_line = None
                    prev_numbered_idx = None
                    empty_lines_before = []

                    k = i - 1
                    while k >= 0:
                        prev_line = lines[k].rstrip()

                        if not prev_line:
                            empty_lines_before.append(k)
                            k -= 1
                            continue

                        # Found a non-empty line, check if it's numbered
                        if numbered_pattern.match(prev_line):
                            prev_numbered_line = prev_line
                            prev_numbered_idx = k

                        # Stop after finding the first non-empty line
                        break

                    # Look forward for numbered line (skip empty lines)
                    next_numbered_line = None
                    next_numbered_idx = None
                    empty_lines_after = []

                    j = i + 1
                    while j < len(lines):
                        next_line = lines[j].rstrip()

                        # Track empty lines
                        if not next_line:
                            empty_lines_after.append(j)
                            j += 1
                            continue

                        # Found a non-empty line, check if it's numbered
                        if numbered_pattern.match(next_line):
                            next_numbered_line = next_line
                            next_numbered_idx = j

                        # Stop after finding the first non-empty line
                        break

                    # Record if we have a numbered line before AND after (must be between two numbered lines)
                    if prev_numbered_line and next_numbered_line:
                        empty_before_count = len(empty_lines_before)
                        empty_after_count = len(empty_lines_after)

                        # Determine if we need to add indentation
                        needs_indent = not already_indented

                        results.append((
                            str(md_file),
                            i + 1,  # Line number (1-indexed)
                            prev_numbered_line,
                            current_line,
                            next_numbered_line,
                            empty_before_count,
                            empty_after_count,
                            needs_indent
                        ))

                        # Prepare modifications if applying fixes
                        if apply_fixes:
                            # Remove empty lines before and after
                            for empty_idx in empty_lines_before:
                                modifications.append(('delete', empty_idx, None))
                            for empty_idx in empty_lines_after:
                                modifications.append(('delete', empty_idx, None))

                            # Add 4-space indentation to the image line (only if not already indented)
                            if needs_indent:
                                indented_image = '    ' + current_line
                                modifications.append(('replace', i, indented_image))

                            # Add empty line before and after the image
                            modifications.append(('insert_before', i, '\n'))
                            modifications.append(('insert_after', i, '\n'))

            # Apply modifications if requested
            if apply_fixes and modifications:
                # Process modifications
                deletes = set()
                replaces = {}
                inserts_before = {}
                inserts_after = {}

                for action, idx, value in modifications:
                    if action == 'delete':
                        deletes.add(idx)
                    elif action == 'replace':
                        replaces[idx] = value
                    elif action == 'insert_before':
                        if idx not in inserts_before:
                            inserts_before[idx] = []
                        inserts_before[idx].append(value)
                    elif action == 'insert_after':
                        if idx not in inserts_after:
                            inserts_after[idx] = []
                        inserts_after[idx].append(value)

                # Apply replacements
                for idx, new_line in replaces.items():
                    if idx < len(modified_lines):
                        modified_lines[idx] = new_line + '\n'

                # Build final result with inserts and deletes
                final_lines = []
                for idx, line in enumerate(modified_lines):
                    # Skip deleted lines
                    if idx in deletes:
                        continue

                    # Insert before
                    if idx in inserts_before:
                        for insert in inserts_before[idx]:
                            final_lines.append(insert)

                    # Add the line itself
                    final_lines.append(line)

                    # Insert after
                    if idx in inserts_after:
                        for insert in inserts_after[idx]:
                            final_lines.append(insert)

                files_to_update[md_file] = final_lines

        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    # Write updated files with Windows line endings
    if apply_fixes and files_to_update:
        print(f"\nApplying fixes to {len(files_to_update)} file(s)...\n")
        for file_path, modified_lines in files_to_update.items():
            try:
                # Join lines and write with Windows line endings (CRLF)
                content = ''.join(modified_lines)
                # Ensure we're writing with CRLF
                content = content.replace('\r\n', '\n').replace('\n', '\r\n')

                with open(file_path, 'w', encoding='utf-8', newline='') as f:
                    f.write(content)

                print(f"Fixed: {file_path}")
            except Exception as e:
                print(f"Error writing {file_path}: {e}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Find and fix whitespace around images in numbered lists'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Apply fixes by adding 4-space indentation and proper empty lines around images'
    )
    parser.add_argument(
        '--docs-dir',
        default='docs',
        help='Directory to search (default: docs)'
    )

    args = parser.parse_args()

    results = find_and_fix_patterns(args.docs_dir, args.apply)

    if not results:
        print("No occurrences found.")
        return

    print(f"Found {len(results)} occurrence(s):\n")
    print("=" * 80)

    for file_path, line_num, prev_numbered, image_line, next_numbered, empty_before, empty_after, needs_indent in results:
        print(f"\nFile: {file_path}")
        print(f"Line: {line_num}")
        print(f"  Previous: {prev_numbered}")
        if empty_before > 0:
            print(f"  Empty lines before image: {empty_before}")
        print(f"  Image:    {image_line}")
        if not needs_indent:
            print(f"  Status:   Already indented (will only add empty lines)")
        if empty_after > 0:
            print(f"  Empty lines after image: {empty_after}")
        print(f"  Next:     {next_numbered}")
        print("-" * 80)

    # Summary
    total_needs_indent = sum(1 for _, _, _, _, _, _, _, needs in results if needs)
    total_with_issues = sum(1 for _, _, _, _, _, before, after, needs in results if before > 0 or after > 0 or needs)
    print(f"\n\nSummary: {len(results)} total occurrence(s) found")
    print(f"  {total_needs_indent} need indentation")
    print(f"  {total_with_issues} need fixes (indentation and/or empty lines)")

    if args.apply:
        print("\nFixes applied! Files saved with Windows line endings (CRLF).")
        print("  - Added 4-space indentation to images (when needed)")
        print("  - Added proper empty lines before and after images")
        print("  - Skipped images in table cells")
        print("  - Skipped adding indentation to already-indented images")
    else:
        print("\nRun with --apply to add indentation and proper spacing around images.")


if __name__ == '__main__':
    main()
