#!/usr/bin/env python3
"""
Script to convert image height attributes to width percentages in markdown files.
Searches recursively through the docs/ directory for markdown files containing
<img> tags with height= attributes and converts them to width="percentage%".
The percentage is calculated as: (original_height / image_height_resolution) * 100

Usage:
    python fix_images_with_height.py                      # Print all images with height attributes
    python fix_images_with_height.py path/to/file.md      # Process single md file (relative to docs/)
    python fix_images_with_height.py path/to/file.md update  # Update image_correct_widths.txt with images from this file
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import cv2
import sys


def load_correct_widths(base_dir: Path) -> Dict[str, str]:
    """
    Load the correct image widths from image_correct_widths.txt.

    Args:
        base_dir: Base directory containing the txt file

    Returns:
        Dictionary mapping normalized image paths to percentage strings
    """
    widths_file = Path(base_dir) / "image_correct_widths.txt"
    correct_widths = {}

    if not widths_file.exists():
        raise RuntimeError(f"Error: File not found: {widths_file}")

    with open(widths_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            # Parse format: "path/to/image.jpg 45%"
            parts = line.rsplit(None, 1)  # Split from right, max 1 split
            if len(parts) != 2:
                raise RuntimeError(f"Warning: Invalid format in {widths_file} line {line_num}: {line}")

            image_path, percentage = parts
            # Normalize path separators and store
            normalized_path = image_path.replace('\\', '/')
            correct_widths[normalized_path] = percentage

    print(f"Loaded {len(correct_widths)} correct width(s) from {widths_file}")

    return correct_widths


def normalize_image_path(src_path: str, md_file_path: Path, docs_dir: Path) -> Optional[str]:
    """
    Normalize an image path to be relative to the docs/ directory.

    Args:
        src_path: The src attribute value from the img tag
        md_file_path: Path to the markdown file
        docs_dir: Base docs directory

    Returns:
        Normalized path relative to docs/ or None if error
    """
    try:
        # Resolve the image path relative to the markdown file
        md_dir = md_file_path.parent
        image_full_path = (md_dir / src_path).resolve()

        # Make it relative to docs directory
        docs_dir_resolved = Path(docs_dir).resolve()
        relative_path = image_full_path.relative_to(docs_dir_resolved)

        # Normalize path separators to forward slashes
        normalized = str(relative_path).replace('\\', '/')

        return normalized

    except Exception as e:
        return None


def get_image_resolution(image_path: Path) -> Tuple[int, int]:
    """
    Get the resolution of an image file using OpenCV.

    Args:
        image_path: Path to the image file

    Returns:
        Tuple of (width, height) or None if error
    """
    img = cv2.imread(str(image_path))
    assert img is not None, f"Error reading image {image_path}"
    height, width = img.shape[:2]
    return (width, height)
    

def extract_img_attributes(img_tag: str) -> Tuple[Optional[str], Optional[int]]:
    """
    Extract src and height attributes from an img tag.

    Args:
        img_tag: The img tag string

    Returns:
        Tuple of (src_path, height_value) or (None, None) if not found
    """
    # Extract src attribute
    src_match = re.search(r'src\s*=\s*["\']([^"\']+)["\']', img_tag, re.IGNORECASE)
    # Extract height attribute
    height_match = re.search(r'height\s*=\s*["\']?(\d+)["\']?', img_tag, re.IGNORECASE)

    src_path = src_match.group(1) if src_match else None
    height_value = int(height_match.group(1)) if height_match else None

    return (src_path, height_value)


def extract_img_width_attribute(img_tag: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract src and width attributes from an img tag.

    Args:
        img_tag: The img tag string

    Returns:
        Tuple of (src_path, width_value) or (None, None) if not found
        e.g. ("Images/foo.jpg", "45%")
    """
    # Extract src attribute
    src_match = re.search(r'src\s*=\s*["\']([^"\']+)["\']', img_tag, re.IGNORECASE)
    # Extract width attribute (can be percentage or pixel value)
    width_match = re.search(r'width\s*=\s*["\']?([^"\'>\s]+)["\']?', img_tag, re.IGNORECASE)

    src_path = src_match.group(1) if src_match else None
    width_value = width_match.group(1) if width_match else None

    return (src_path, width_value)


def convert_height_to_width_percentage(
    img_tag: str,
    md_file_path: Path,
    docs_dir: Path,
    correct_widths: Dict[str, str]
) -> str:
    """
    Convert an img tag with height attribute to use width percentage instead.

    Args:
        img_tag: The original img tag string
        md_file_path: Path to the markdown file containing the tag
        docs_dir: Base docs directory
        correct_widths: Dictionary of image path -> correct percentage

    Returns:
        Modified img tag string or original if conversion fails
    """
    src_path, height_value = extract_img_attributes(img_tag)

    if not src_path or not height_value:
        print(f"  Warning: Could not extract src or height from tag: {img_tag}")
        return img_tag

    # Check if width attribute already exists
    if re.search(r'width\s*=', img_tag, re.IGNORECASE):
        print(f"  Warning: Image already has width attribute, skipping: {src_path}")
        return img_tag

    # Resolve image path relative to the markdown file
    md_dir = md_file_path.parent
    image_full_path = (md_dir / src_path).resolve()

    if not image_full_path.exists():
        print(f"  Warning: Image file not found: {image_full_path}")
        return img_tag

    # Normalize image path to check against correct_widths
    normalized_path = normalize_image_path(src_path, md_file_path, docs_dir)

    # Check if we have a correct width for this image
    if normalized_path and normalized_path in correct_widths:
        percentage_str = correct_widths[normalized_path]
        print(f"  Converted: {src_path} -> width={percentage_str} [from correct_widths.txt]")

        # Remove height attribute and add width percentage
        new_tag = re.sub(r'\s*height\s*=\s*["\']?\d+["\']?', '', img_tag, flags=re.IGNORECASE)
        new_tag = new_tag.rstrip('>').rstrip() + f' width="{percentage_str}">'

        return new_tag

    # Otherwise, calculate percentage from image resolution
    resolution = get_image_resolution(image_full_path)

    img_width, img_height = resolution
    assert img_height > 0, f"Error: image height 0 at {image_full_path}"

    # Calculate percentage: (height_attribute / image_height) * 100
    percentage = (height_value / img_height) * 100

    # Round to 1 decimal place
    percentage = round(percentage, 1)

    # Remove height attribute and add width percentage
    # First remove the height attribute
    new_tag = re.sub(r'\s*height\s*=\s*["\']?\d+["\']?', '', img_tag, flags=re.IGNORECASE)

    # Add width percentage before the closing >
    new_tag = new_tag.rstrip('>').rstrip() + f' width="{percentage}%">'

    print(f"  Converted: {src_path} (height={height_value}, img_height={img_height}) -> width={percentage}% [calculated]")

    return new_tag


def process_markdown_file(md_file: Path, docs_dir: Path, correct_widths: Dict[str, str]) -> int:
    """
    Process a markdown file and convert height attributes to width percentages.

    Args:
        md_file: Path to the markdown file
        docs_dir: Base docs directory
        correct_widths: Dictionary of image path -> correct percentage

    Returns:
        Number of conversions made
    """
    # Pattern to match <img> tags with height attribute but no width attribute
    img_height_pattern = re.compile(r'<img[^>]*height\s*=\s*["\']?\d+["\']?[^>]*>', re.IGNORECASE)

    try:
        # Read the file
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        conversions = 0

        # Find all img tags with height
        for match in img_height_pattern.finditer(original_content):
            img_tag = match.group(0)

            # Skip if it already has width attribute
            if re.search(r'width\s*=', img_tag, re.IGNORECASE):
                continue

            new_tag = convert_height_to_width_percentage(img_tag, md_file, docs_dir, correct_widths)

            if new_tag != img_tag:
                content = content.replace(img_tag, new_tag)
                conversions += 1

        # Write back with Windows line endings (CRLF) if changes were made
        if conversions > 0:
            # Convert to Windows line endings
            content = content.replace('\r\n', '\n').replace('\n', '\r\n')

            with open(md_file, 'w', encoding='utf-8', newline='') as f:
                f.write(content)

        return conversions

    except Exception as e:
        print(f"Error processing {md_file}: {e}")
        return 0


def extract_images_with_width(md_file: Path, docs_dir: Path) -> List[Tuple[str, str]]:
    """
    Extract all images with width attributes from a markdown file.

    Args:
        md_file: Path to the markdown file
        docs_dir: Base docs directory

    Returns:
        List of tuples (normalized_path, width_value)
        e.g. [("SetupGuide/Images/foo.jpg", "45%"), ...]
    """
    # Pattern to match <img> tags with width attribute
    img_width_pattern = re.compile(r'<img[^>]*width\s*=\s*["\']?[^"\'>\s]+["\']?[^>]*>', re.IGNORECASE)

    images: List[Tuple[str, str]] = []

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all img tags with width
    for match in img_width_pattern.finditer(content):
        img_tag = match.group(0)
        src_path, width_value = extract_img_width_attribute(img_tag)

        if src_path and width_value:
            # Normalize the image path relative to docs directory
            normalized_path = normalize_image_path(src_path, md_file, docs_dir)
            if normalized_path:
                images.append((normalized_path, width_value))

    return images


def update_correct_widths_file(
    base_dir: Path,
    new_entries: List[Tuple[str, str]],
    existing_widths: Dict[str, str]
) -> int:
    """
    Append new image width entries to image_correct_widths.txt.

    Args:
        base_dir: Base directory containing the txt file
        new_entries: List of (normalized_path, width_value) tuples to add
        existing_widths: Dictionary of already existing image paths

    Returns:
        Number of new entries added
    """
    widths_file = Path(base_dir) / "image_correct_widths.txt"

    # Filter out entries that already exist
    entries_to_add: List[Tuple[str, str]] = []
    for path, width in new_entries:
        if path not in existing_widths:
            entries_to_add.append((path, width))

    if not entries_to_add:
        print("No new entries to add to image_correct_widths.txt")
        return 0

    # Append new entries to the file
    with open(widths_file, 'a', encoding='utf-8') as f:
        for path, width in entries_to_add:
            f.write(f"{path} {width}\n")
            print(f"  Added: {path} {width}")

    return len(entries_to_add)


def find_images_with_height(docs_dir: Path) -> List[Tuple[str, int, str]]:
    """
    Find all markdown files with image tags that have height attributes.

    Args:
        docs_dir: Path to the docs directory to search

    Returns:
        List of tuples (file_path, line_number, matched_line)
    """
    # Pattern to match <img> tags with height attribute
    img_height_pattern = re.compile(r'<img[^>]*height\s*=\s*["\']?\d+["\']?[^>]*>', re.IGNORECASE)

    results: List[Tuple[str, int, str]] = []

    # Find all markdown files
    for md_file in Path(docs_dir).rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                if img_height_pattern.search(line):
                    # Get relative path from docs directory parent
                    rel_path = str(md_file.relative_to(Path(docs_dir).parent))
                    results.append((rel_path, line_num, line.strip()))

    return results


def print_images_with_height(docs_dir: Path) -> None:
    """
    Print all images with height attributes found in markdown files.

    Args:
        docs_dir: Path to the docs directory to search
    """
    results = find_images_with_height(docs_dir)

    if not results:
        print("No images with height attributes found.")
        return

    # Group by file
    files_dict: Dict[str, List[Tuple[int, str]]] = {}
    for file_path, line_num, line in results:
        if file_path not in files_dict:
            files_dict[file_path] = []
        files_dict[file_path].append((line_num, line))

    # Print results
    print(f"Found {len(results)} image(s) with height attributes in {len(files_dict)} file(s):\n")

    for file_path in sorted(files_dict.keys()):
        print(f"\n{file_path}:")
        print("-" * 80)
        for line_num, line in files_dict[file_path]:
            print(f"  Line {line_num}: {line}")

    print("\n" + "=" * 80)
    print(f"\nTotal: {len(results)} image(s) in {len(files_dict)} file(s)")


def find_and_convert_images(
    docs_dir: Path,
    correct_widths: Dict[str, str],
    single_file: Optional[str] = None
) -> Tuple[int, int]:
    """
    Find all markdown files with image tags that have height attributes and convert them.

    Args:
        docs_dir: Path to the docs directory to search
        correct_widths: Dictionary of image path -> correct percentage
        single_file: If provided, only process this single file (relative to docs_dir)

    Returns:
        Tuple of (total_conversions, files_modified)
    """
    total_conversions = 0
    files_modified = 0

    # If single file is specified, only process that file
    if single_file:
        md_file = Path(docs_dir) / single_file

        if not md_file.exists():
            raise RuntimeError(f"Error: File not found: {md_file}")

        if not md_file.suffix == '.md':
            raise RuntimeError(f"Error: File is not a markdown file: {md_file}")

        print(f"Processing single file: {single_file}")

        conversions = process_markdown_file(md_file, docs_dir, correct_widths)

        if conversions > 0:
            total_conversions += conversions
            files_modified += 1
            print(f"  Modified {conversions} image(s)")
        else:
            print(f"  No conversions needed")

        return (total_conversions, files_modified)

    # Otherwise, find all markdown files
    for md_file in Path(docs_dir).rglob('*.md'):
        rel_path = md_file.relative_to(Path(docs_dir).parent)
        print(f"\nProcessing: {rel_path}")

        conversions = process_markdown_file(md_file, docs_dir, correct_widths)

        if conversions > 0:
            total_conversions += conversions
            files_modified += 1
            print(f"  Modified {conversions} image(s)")

    return (total_conversions, files_modified)


def main() -> None:
    """Main entry point for the script."""
    # Get the docs directory
    base_dir = Path(__file__).parent
    docs_dir = base_dir / "docs"

    # Load correct widths from txt file, relative image path -> str of percentage
    # e.g. "SetupGuide/Images/ArduinoLeonardo/ControllerSetup-Leonardo.jpg" -> "45%"
    correct_widths = load_correct_widths(base_dir)

    # Parse command line arguments
    update_mode = False
    single_file: Optional[str] = None

    if len(sys.argv) > 1:
        single_file = sys.argv[1]
        # Check if second argument is "update"
        if len(sys.argv) > 2 and sys.argv[2].lower() == "update":
            update_mode = True

    # Update mode: extract images with width from md file and add to image_correct_widths.txt
    if update_mode:
        if not single_file:
            raise RuntimeError("Error: Update mode requires a markdown file path")

        md_file = Path(docs_dir) / single_file

        if not md_file.exists():
            raise RuntimeError(f"Error: File not found: {md_file}")

        if not md_file.suffix == '.md':
            raise RuntimeError(f"Error: File is not a markdown file: {md_file}")

        print(f"Update mode: Extracting images from {single_file}")
        print("=" * 80)

        # Extract all images with width attributes
        images = extract_images_with_width(md_file, docs_dir)

        if not images:
            print("No images with width attributes found in the file")
            return

        print(f"Found {len(images)} image(s) with width attributes")

        # Update the correct_widths.txt file
        new_entries_count = update_correct_widths_file(base_dir, images, correct_widths)

        print("\n" + "=" * 80)
        print(f"\nAdded {new_entries_count} new entry(ies) to image_correct_widths.txt")
        return

    # Print mode: no arguments, print all images with height attributes
    if not single_file:
        print(f"Searching for images with height attributes in: {docs_dir}")
        print("=" * 80)
        print_images_with_height(docs_dir)
        return

    # Convert mode: process single file
    print(f"Single file mode: {single_file}")
    print("=" * 80)

    total_conversions, files_modified = find_and_convert_images(docs_dir, correct_widths, single_file)

    print("\n" + "=" * 80)
    print(f"\nTotal: {total_conversions} image(s) converted in {files_modified} file(s)")
    print("\nAll modified files have been saved with Windows line endings (CRLF).")


if __name__ == "__main__":
    main()
