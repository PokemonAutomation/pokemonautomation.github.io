#!/usr/bin/env python3
"""
Find and fix list indentation in markdown files.

Searches for list lines (starting with "-") that have exactly 3 spaces of indentation.
With --apply flag, fixes them to have 4 spaces of indentation.
"""

import argparse
import os
import re
from pathlib import Path


def find_and_fix_list_indentation(docs_dir='docs', apply_fixes=False):
    """
    Search for list lines with 3-space indentation.
    Optionally fix them to use 4-space indentation.

    Args:
        docs_dir: Directory to search (default: 'docs')
        apply_fixes: If True, apply fixes and save files

    Returns:
        List of tuples: (file_path, line_number, line_content, context_before, context_after)
    """
    results = []
    files_to_update = {}  # file_path -> modified_lines

    # Pattern for list lines with exactly 3 spaces before the dash
    # ^   -  means: start of line, exactly 3 spaces, then a dash
    three_space_list_pattern = re.compile(r'^   -\s')

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

            lines_to_fix = []  # Track indices of lines to fix

            # Check each line for 3-space indented list
            for i in range(len(lines)):
                current_line = lines[i]

                # Check if current line matches the pattern
                if three_space_list_pattern.match(current_line):
                    # Get context: 2 lines before and 2 lines after
                    context_before = []
                    context_after = []

                    # Get 2 lines before
                    for j in range(max(0, i - 2), i):
                        context_before.append((j + 1, lines[j].rstrip()))

                    # Get 2 lines after
                    for j in range(i + 1, min(len(lines), i + 3)):
                        context_after.append((j + 1, lines[j].rstrip()))

                    results.append((
                        str(md_file),
                        i + 1,  # Line number (1-indexed)
                        current_line.rstrip(),
                        context_before,
                        context_after
                    ))

                    # Mark for fixing if applying
                    if apply_fixes:
                        lines_to_fix.append(i)

            # Apply fixes if requested
            if apply_fixes and lines_to_fix:
                modified_lines = lines.copy()

                # Fix each line by replacing 3 spaces with 4 spaces at the start
                for idx in lines_to_fix:
                    # Replace "   -" with "    -" at the start of the line
                    modified_lines[idx] = '    ' + lines[idx][3:]

                files_to_update[md_file] = modified_lines

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
        description='Find and fix list indentation (3 spaces -> 4 spaces) in markdown files'
    )
    parser.add_argument(
        '--apply',
        action='store_true',
        help='Apply fixes by changing 3-space indentation to 4-space indentation'
    )
    parser.add_argument(
        '--docs-dir',
        default='docs',
        help='Directory to search (default: docs)'
    )

    args = parser.parse_args()

    results = find_and_fix_list_indentation(args.docs_dir, args.apply)

    if not results:
        print("No occurrences found.")
        return

    print(f"Found {len(results)} list line(s) with 3-space indentation:\n")
    print("=" * 80)

    for file_path, line_num, line_content, context_before, context_after in results:
        print(f"\nFile: {file_path}")
        print(f"Line: {line_num}")
        print()

        # Print 2 lines before
        for ctx_line_num, ctx_line in context_before:
            print(f"  {ctx_line_num:4d}: {ctx_line}")

        # Print the problematic line (highlighted)
        print(f"→ {line_num:4d}: {line_content}")

        # Print 2 lines after
        for ctx_line_num, ctx_line in context_after:
            print(f"  {ctx_line_num:4d}: {ctx_line}")

        print("-" * 80)

    # Summary
    print(f"\n\nSummary: {len(results)} list line(s) with 3-space indentation found")

    if args.apply:
        files_fixed = len(set(r[0] for r in results))
        print(f"\nFixes applied to {files_fixed} file(s)! Files saved with Windows line endings (CRLF).")
        print("  - Changed 3-space indentation to 4-space indentation for list items")
    else:
        print("\nRun with --apply to fix indentation and save files.")


if __name__ == '__main__':
    main()
