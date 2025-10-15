#!/usr/bin/env python3
"""
Script to fix old GitHub wiki links to point to new documentation.
Searches for links containing "github.com/PokemonAutomation/ComputerControl/blob/master"
and converts them to point to the new docs/ directory.

Usage:
    python fix_wiki_links.py           # Print all old wiki links and check if new docs exist
    python fix_wiki_links.py --apply   # Apply the link replacements
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def extract_markdown_links(content: str) -> List[Tuple[str, str, int]]:
    """
    Extract all markdown links from content.

    Args:
        content: The markdown content

    Returns:
        List of tuples (link_text, url, position)
        e.g. [("Setup Guide", "https://...", 123), ...]
    """
    # Pattern to match markdown links: [text](url)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    links: List[Tuple[str, str, int]] = []
    for match in link_pattern.finditer(content):
        link_text = match.group(1)
        url = match.group(2)
        position = match.start()
        links.append((link_text, url, position))

    return links


def is_old_wiki_link(url: str) -> bool:
    """
    Check if a URL is an old GitHub wiki link.

    Args:
        url: The URL to check

    Returns:
        True if it's an old wiki link
    """
    return "github.com/PokemonAutomation/ComputerControl/blob/master" in url


def convert_github_link_to_docs_path(url: str) -> Optional[str]:
    """
    Convert old GitHub wiki link to new docs path.

    Args:
        url: The old GitHub URL
        e.g. "https://github.com/PokemonAutomation/ComputerControl/blob/master/Wiki/SetupGuide.md"

    Returns:
        New docs path relative to docs/ directory
        e.g. "SetupGuide.md" or None if conversion not possible
    """
    if not is_old_wiki_link(url):
        return None

    # Extract the path after "blob/master/"
    match = re.search(r'blob/master/(.+?)(?:#.*)?$', url)
    if not match:
        return None

    path = match.group(1)

    # Remove "Wiki/" prefix if present
    if path.startswith("Wiki/"):
        path = path[5:]  # Remove "Wiki/"

    # Handle "Documentation/" prefix
    if path.startswith("Documentation/"):
        path = path[14:]  # Remove "Documentation/"

    return path


def check_docs_file_exists(docs_dir: Path, relative_path: str) -> bool:
    """
    Check if a docs file exists.

    Args:
        docs_dir: Base docs directory
        relative_path: Path relative to docs/ directory

    Returns:
        True if file exists
    """
    full_path = docs_dir / relative_path
    return full_path.exists()


def convert_to_relative_link(from_file: Path, to_file: Path, docs_dir: Path) -> str:
    """
    Convert absolute docs path to relative link from source file.

    Args:
        from_file: The markdown file containing the link
        to_file: The target file in docs/
        docs_dir: Base docs directory

    Returns:
        Relative path from from_file to to_file
        e.g. "../SetupGuide.md" or "Images/foo.jpg"
    """
    try:
        # Get the directory containing the source file
        from_dir = from_file.parent

        # Calculate relative path
        relative = to_file.relative_to(from_dir)
        return str(relative).replace('\\', '/')
    except ValueError:
        # If relative_to fails, try using relative path calculation
        from_parts = from_file.parent.parts
        to_parts = to_file.parts

        # Find common prefix
        common_length = 0
        for i, (f, t) in enumerate(zip(from_parts, to_parts)):
            if f == t:
                common_length = i + 1
            else:
                break

        # Calculate relative path
        up_count = len(from_parts) - common_length
        relative_parts = ['..'] * up_count + list(to_parts[common_length:])

        return '/'.join(relative_parts)


def find_old_wiki_links(docs_dir: Path) -> List[Tuple[Path, int, str, str, Optional[str], bool]]:
    """
    Find all old wiki links in markdown files.

    Args:
        docs_dir: Base docs directory

    Returns:
        List of tuples (file_path, line_number, full_link, old_url, new_path, exists)
        e.g. [(Path("docs/foo.md"), 10, "[text](url)", "old_url", "new_path", True), ...]
    """
    results: List[Tuple[Path, int, str, str, Optional[str], bool]] = []

    # Find all markdown files
    for md_file in docs_dir.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

        # Extract links
        links = extract_markdown_links(content)

        for link_text, url, position in links:
            if is_old_wiki_link(url):
                # Find line number
                line_num = content[:position].count('\n') + 1

                # Convert to new docs path
                new_path = convert_github_link_to_docs_path(url)

                # Check if new docs file exists
                exists = False
                if new_path:
                    exists = check_docs_file_exists(docs_dir, new_path)

                # Store the full link text for replacement
                full_link = f"[{link_text}]({url})"

                results.append((md_file, line_num, full_link, url, new_path, exists))

    return results


def print_old_wiki_links(docs_dir: Path) -> None:
    """
    Print all old wiki links and report if new docs exist.

    Args:
        docs_dir: Base docs directory
    """
    results = find_old_wiki_links(docs_dir)

    if not results:
        print("No old wiki links found.")
        return

    # Group by file
    files_dict: Dict[Path, List[Tuple[int, str, str, Optional[str], bool]]] = {}
    # Track missing links for summary at the end: new_path -> list of (file, line_num, old_url)
    missing_links: Dict[Optional[str], List[Tuple[Path, int, str]]] = {}

    for file_path, line_num, full_link, old_url, new_path, exists in results:
        if file_path not in files_dict:
            files_dict[file_path] = []
        files_dict[file_path].append((line_num, full_link, old_url, new_path, exists))

        # Track missing links
        if not exists:
            if new_path not in missing_links:
                missing_links[new_path] = []
            missing_links[new_path].append((file_path, line_num, old_url))

    # Print results
    print(f"Found {len(results)} old wiki link(s) in {len(files_dict)} file(s):\n")

    found_count = 0
    missing_count = 0

    for file_path in sorted(files_dict.keys()):
        rel_path = file_path.relative_to(docs_dir.parent)
        print(f"\n{rel_path}:")
        print("-" * 80)

        for line_num, full_link, old_url, new_path, exists in files_dict[file_path]:
            status = "✓ EXISTS" if exists else "✗ MISSING"
            if exists:
                found_count += 1
            else:
                missing_count += 1

            print(f"  Line {line_num}: {full_link}")
            print(f"    Old: {old_url}")
            if new_path:
                print(f"    New: {new_path} [{status}]")
            else:
                print(f"    New: [Cannot convert]")

    print("\n" + "=" * 80)
    print(f"\nTotal: {len(results)} old wiki link(s)")
    print(f"  ✓ {found_count} have corresponding new docs")
    print(f"  ✗ {missing_count} are missing in new docs")

    # Print missing links summary
    if missing_links:
        print("\n" + "=" * 80)
        print("\nMissing Links Summary:")
        print("The following files are referenced but not found in docs/:\n")

        for new_path in sorted(missing_links.keys(), key=lambda x: x if x else ""):
            if new_path:
                print(f"\n  {new_path}")
            else:
                print(f"\n  [Cannot convert path]")
            print("  " + "-" * 78)

            for file_path, line_num, old_url in missing_links[new_path]:
                rel_path = file_path.relative_to(docs_dir.parent)
                print(f"    Referenced in: {rel_path}:{line_num}")
                print(f"      {old_url}")


def apply_link_fixes(docs_dir: Path) -> None:
    """
    Apply link replacements to all markdown files.

    Args:
        docs_dir: Base docs directory
    """
    results = find_old_wiki_links(docs_dir)

    if not results:
        print("No old wiki links found.")
        return

    # Group by file
    files_dict: Dict[Path, List[Tuple[int, str, str, Optional[str], bool]]] = {}
    for file_path, line_num, full_link, old_url, new_path, exists in results:
        if file_path not in files_dict:
            files_dict[file_path] = []
        files_dict[file_path].append((line_num, full_link, old_url, new_path, exists))

    total_replaced = 0
    total_skipped = 0
    files_modified = 0

    for md_file in sorted(files_dict.keys()):
        print(f"\nProcessing: {md_file.relative_to(docs_dir.parent)}")

        # Read file content
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        replaced_in_file = 0
        skipped_in_file = 0

        for line_num, full_link, old_url, new_path, exists in files_dict[md_file]:
            if exists and new_path:
                # Calculate relative link from current file to target
                target_file = docs_dir / new_path
                relative_link = convert_to_relative_link(md_file, target_file, docs_dir)

                # Extract link text from full_link
                match = re.match(r'\[([^\]]+)\]\([^)]+\)', full_link)
                if match:
                    link_text = match.group(1)
                    new_link = f"[{link_text}]({relative_link})"

                    # Replace in content
                    if full_link in content:
                        content = content.replace(full_link, new_link, 1)
                        print(f"  Line {line_num}: Replaced")
                        print(f"    Old: {old_url}")
                        print(f"    New: {relative_link}")
                        replaced_in_file += 1
                    else:
                        print(f"  Line {line_num}: Warning - link not found for replacement")
                        skipped_in_file += 1
            else:
                print(f"  Line {line_num}: Skipped (target missing: {new_path})")
                skipped_in_file += 1

        # Write back if changes were made
        if content != original_content:
            # Convert to Windows line endings
            content = content.replace('\r\n', '\n').replace('\n', '\r\n')

            with open(md_file, 'w', encoding='utf-8', newline='') as f:
                f.write(content)

            files_modified += 1
            print(f"  Modified: {replaced_in_file} link(s) replaced, {skipped_in_file} skipped")

        total_replaced += replaced_in_file
        total_skipped += skipped_in_file

    print("\n" + "=" * 80)
    print(f"\nTotal: {total_replaced} link(s) replaced, {total_skipped} skipped")
    print(f"Files modified: {files_modified}")
    print("\nAll modified files have been saved with Windows line endings (CRLF).")


def main() -> None:
    """Main entry point for the script."""
    # Get the docs directory
    base_dir = Path(__file__).parent
    docs_dir = base_dir / "docs"

    if not docs_dir.exists():
        raise RuntimeError(f"Error: docs directory not found: {docs_dir}")

    # Parse command line arguments
    apply_mode = False
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        apply_mode = True

    if apply_mode:
        print("Apply mode: Fixing old wiki links")
        print("=" * 80)
        apply_link_fixes(docs_dir)
    else:
        print(f"Searching for old wiki links in: {docs_dir}")
        print("=" * 80)
        print_old_wiki_links(docs_dir)
        print("\nTo apply fixes, run: python fix_wiki_links.py --apply")


if __name__ == "__main__":
    main()
