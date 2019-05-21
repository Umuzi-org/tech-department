"""
This is a Python3.7 script that makes sure that markdown files are named correctly.
It also highlights any metadata problems (specifically missing titles)
"""
import logging
import os
from pathlib import Path
import frontmatter


def fixup(path):
    location = Path(path)
    assert location.is_dir(), location
    for child in location.iterdir():
        if child.is_dir():
            fixup(child)
        else:
            check_metadata(child)
            # fix_file(child)


def fix_file(file_path):
    name = file_path.name
    if not name.endswith(".md"):
        # we only care about markdown files.
        return
    if name.startswith("_index."):
        # looks good
        return
    # make a directory with the same name as the file (without the extension)
    suffix = "".join(file_path.suffixes)
    prefix = name[: -len(suffix)]

    new_dir = file_path.parent / prefix
    new_dir.mkdir()

    new_path = new_dir / f"_index{suffix}"
    file_path.rename(new_path)


def check_metadata(file_path):
    """ given the path to a markdown file, make sure that the frontmatter includes
    the required metadata
    """
    logger = logging.getLogger(__name__)
    name = file_path.name
    if not name.endswith(".md"):
        return
    post = frontmatter.load(file_path)

    required = ["title"]
    allowed = ["pre", "weight", "ready", "date", "disableToc"]

    for key in post.keys():
        if key not in required + allowed:
            logger.warn(f"{file_path} has unrecognized frontmatter: {key}")
            continue
    for key in required:
        if key not in post.keys():
            logger.error(f"{file_path} has MISSING frontmatter: {key}")
            continue


if __name__ == "__main__":
    fixup("content")

