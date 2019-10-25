"""Entrypoint module for application"""
import os
import sys
from pathlib import Path
import argparse
from fnmatch import fnmatch
from verse import Verse
from inserts import insert

FLAGS = None

def resolve_path(filename):
    """Resolve absolute path for filename"""
    return str(Path(filename).resolve())

def get_files(directory, pattern="*.txt"):
    """Get list of files to parse and insert"""
    _dir = resolve_path(directory)
    files = [f'{_dir}/{file}' for file in os.listdir(_dir) if fnmatch(file, pattern)]
    if files == []:
        print(f'No files matching {pattern} found in {resolve_path(directory)}')
        sys.exit(0)
    else:
        return files

def read_file(filename):
    """
    Read file contents line by line

    This method uses a generator to reduce
    the in-memory burden of iterating over
    many, large text files.
    """
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            yield line

def main(directory='.'):
    """Entrypoint for application"""
    for file in get_files(directory, '*.txt'):
        print(file)
        # verses = [Verse(line, 'Proverbs') for line in read_file(file)]
        verses = [line for line in read_file(file)]
        for verse in verses:
            print(verse)
            # insert(verse)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dir',
        type=str,
        default='.')
    FLAGS, unparsed = parser.parse_known_args()
    main(FLAGS.dir)
