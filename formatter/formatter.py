"""Formater for starter texts"""
import os
import sys
from fnmatch import fnmatch

def stop_execution(msg="There was a problem"):
    """General halt method for errors"""
    print(msg)
    sys.exit(1)

def get_files(directory="."):
    """Return list of file names from given directory"""
    return [file for file in os.listdir(directory) if fnmatch(file, "*.txt")]

def iterator(iterable, iter_func, err_msg="Cannot iterate over empty list"):
    """Iterator over iterable"""
    if iterable == []:
        stop_execution(err_msg)

    return [iter_func(i) for i in iterable]

def add_new_lines(chapter, line):
    """Add \n to string"""
    newline = ""
    for char in line:
        if char.isdigit():
            newline += f'\n{chapter}:{char}'
        else:
            newline += char
    return f'{chapter}\n{newline}'

def parse_line_contents(line):
    """
    Parse content of line

    If line begins with '#', it is a chapter line
    and chapter count should increase

    Else the line contains the chapter text
    """
    current_chapter = 0

    if line[0] == "#":
        current_chapter += 1
        return

    return add_new_lines(current_chapter, line)

def read_file(file):
    """Read files for content"""
    f = open(file, "r")
    return f.readlines()

def write_to_file(filename):
    """Write contents to new file"""
    f = open(filename, "w+")

def main(directory="."):
    """Entrypoint"""
    files = get_files(directory)
    lines = iterator(files, read_file, "No files found matching .txt found")
    parsed_lines = iterator(lines, parse_line_contents, "File contents empty")

if __name__ == "__main__":
    main(sys.argv[1])
