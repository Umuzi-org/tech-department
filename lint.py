"""
This is a Python3.7 script that makes sure that markdown files are named correctly.
It also highlights any metadata problems (specifically missing titles)
"""
import logging
import os
from pathlib import Path

def fixup(path):
    location = Path(path)
    assert location.is_dir(), location
    for child in location.iterdir():
        if child.is_dir():
            fixup(child)
        else:
            fix_file(child)


def fix_file(file_path):
    name = file_path.name
    if not name.endswith(".md"):
        # we only care about markdown files.
        return
    check_metadata(file_path)
    if name.startswith("_index."):
        # looks good
        return
    # make a directory with the same name as the file (without the extension)
    suffix = ''.join(file_path.suffixes)
    prefix = name[: -len(suffix)]

    new_dir = file_path.parent / prefix
    new_dir.mkdir()

    new_path = new_dir / f"_index{suffix}"
    file_path.rename(new_path)



def check_metadata(file_path):
    """ given the path to a markdown file, make sure that the frontmatter includes
    the required metadata
    """
    # TODO
    # required = ['title']
    # allowed  = ['pre', 'weight', 'ready']

if __name__ == '__main__':
    fixup('content')



