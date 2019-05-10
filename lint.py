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

if __name__ == '__main__':
    fixup('content')



    [ '', 'anchor', 'as_posix', '', 'chmod', 'cwd', 'drive', 'exists', 'expanduser', 'glob', 'group', , 'is_absolute', 'is_block_device', 'is_char_device', 'is_dir', 'is_fifo', '', 'is_mount', , 'iterdir', , , 'lstat', 'match', 'mkdir', 'name', 'open', , 'parent', 'parents', 'parts', 'read_bytes', 'read_text', 'relative_to', 'rename', 'replace', 'resolve', '', 'rmdir', 'root', 'samefile', 'stat', 'stem', 'suffix', 'suffixes', 'symlink_to', 'touch', 'unlink', 'with_name', 'with_suffix', 'write_bytes', 'write_text']