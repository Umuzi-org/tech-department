from pathlib import Path
import os
import re
import youtube_dl

OUTPUT_DIR = Path("downloaded_videos")
os.makedirs(OUTPUT_DIR, exist_ok=True)
CONTENT_DIR = Path("content")


def generate_youtube_links(path):
    """ go through all the markdown files in content and yield all the youtube urls.
    """
    if path.is_dir():
        for child in os.listdir(path):
            for link in generate_youtube_links(path / child):
                yield link
    elif path.suffix == ".md":
        with open(path, "r") as f:
            for line in f:
                found = re.search("\((https://youtu.*)\)", line)
                if found:
                    for link in found.groups():
                        yield path, link


def main():
    cwd = os.getcwd()
    for path, link in generate_youtube_links(CONTENT_DIR):
        final_dir = OUTPUT_DIR / path.relative_to(CONTENT_DIR).parent
        os.makedirs(final_dir, exist_ok=True)
        os.chdir(final_dir)
        with youtube_dl.YoutubeDL({}) as ydl:
            ydl.download([link])
        os.chdir(cwd)


if __name__ == "__main__":
    main()

