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
    """Parse contents"""
    current_chapter = 0

    if line[0] == "#":
        current_chapter += 1

    return ""

def read_file(file):
    """Read files for content"""
    f = open(file, "r")
    lines = f.readlines()
    for line in lines:
        parse_line_contents(line)

def write_to_file(filename):
    """Write contents to new file"""
    f = open(filename, "w+")

def iter_files(files):
    """Iterator over files"""
    if files == []:
        stop_execution("No files found that match the pattern *.txt")

    read_files = [read_file(f) for f in files]
    return "yep"

def main(directory="."):
    """Entrypoint"""
    files = get_files(directory)
    error_or_success = iter_files(files)

if __name__ == "__main__":
    main()
