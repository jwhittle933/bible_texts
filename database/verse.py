"""ORM module"""
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Verse(Base):
    """MT Text class for ORM"""
    __tablename__ = 'lxx_text'

    line = ""
    id = Column(Integer, primary_key=True)
    book = Column(String(20))
    chapter = Column(Integer)
    verse = Column(Integer)
    text = Column(Text)
    notes = Column(Text)

    def __init__(self, line, book):
        """Init class with line of text"""
        self.line = line
        self.book = book

    def __repr__(self):
        return "<Verse(line='%s')>" % (self.line)

    def parse_line(self):
        """Parse line content for chapter, verse, and text"""
        return self

    def add_note(self, notes):
        """Add notes to instace of verse"""
        self.notes = notes
        return self
