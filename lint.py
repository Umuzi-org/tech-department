"""
This is a Python3.7 script that makes sure that markdown files are named correctly.
It also highlights any metadata problems (specifically missing titles)
"""
import logging
import os
from pathlib import Path
import frontmatter


def check_all_frontmatter(path):
    location = Path(path)
    assert location.is_dir(), location
    for child in location.iterdir():
        if child.is_dir():
            check_all_frontmatter(child)
        else:
            check_one_file_frontmatter(child)


# def fix_file(file_path):
#     """ take a file at a specific path and change it as follows

#     path/to/some/awesome_topic.md
#     =>
#     path/to/some/awesome_topic/_index.md

#     probably no longer needed
#     """
#     name = file_path.name
#     if not name.endswith(".md"):
#         # we only care about markdown files.
#         return
#     if name.startswith("_index."):
#         # looks good
#         return
#     # make a directory with the same name as the file (without the extension)
#     suffix = "".join(file_path.suffixes)
#     prefix = name[: -len(suffix)]

#     new_dir = file_path.parent / prefix
#     new_dir.mkdir()

#     new_path = new_dir / f"_index{suffix}"
#     file_path.rename(new_path)


def check_one_file_frontmatter(file_path):
    """ given the path to a markdown file, make sure that the frontmatter includes
    the required metadata
    """
    logger = logging.getLogger(__name__)
    name = file_path.name
    if not name.endswith(".md"):
        return
    post = frontmatter.load(file_path)

    required = ["title"]
    allowed = ["pre", "weight", "ready", "date", "disableToc", "todo", "attn","noform","ncit_unit_standard","ncit_specific_outcomes"]

    for key in post.keys():
        if key not in required + allowed:
            logger.warning(f"{file_path} has unrecognized frontmatter: {key}")
            continue
    for key in required:
        if key not in post.keys():
            logger.error(f"{file_path} has MISSING frontmatter: {key}")
            continue


def check_contentlinks_ok():
    import os
    os.system("hugo")
    os.system('grep -r "contentlink-missing" public')  # TODO
    os.system('grep -r "contentlink-todo" public')  # TODO


if __name__ == "__main__":
    check_all_frontmatter("content")


