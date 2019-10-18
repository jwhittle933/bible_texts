"""Module Text"""
import os
import sys

class Text():
    """Text class for reading, parsing, and writing text files"""
    current_chapter = 0
    lines = []

    def __init__(self, file):
        self.file = file

    def read(self):
        """Read method"""
        file = open(self.file)
        self.lines = file.readlines()

    @classmethod
    def parse_line(cls):
        """Parse method"""
        for line in cls.lines:
            if line[0] == "#":
                cls.current_chapter += 1
        return ""

    def write(self):
        """Write method"""
        return ""


    @classmethod
    def stop_execution(cls, msg):
        """General halt method for errors"""
        print(msg)
        sys.exit(0)
