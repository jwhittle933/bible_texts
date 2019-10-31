"""LXX Tables Migration"""
from sqlalchemy import Table, Column, Integer, Text, MetaData

META = MetaData()
BOOKS = ['genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy',
         'joshua', 'judges', 'ruth', '1reigns', '2reigns', '3reigns',
         '4reigns', '1paraleipomenon', '2paraleipomenon', '1esdras', '2esdras',
         'esther', 'judith', 'tobit', '1maccabees', '2maccabees',
         '3maccabees', '4maccabees', 'psalms', 'odes', 'proverbs',
         'ecclesiastes', 'songofsolomon', 'job', 'wisdomofsolomon',
         'sirach', 'psalmsofsolomon', 'hosea', 'amos', 'micah', 'joel',
         'obadiah', 'jonah', 'nahum', 'habbakuk', 'zephaniah', 'haggai',
         'zechariah', 'malachi', 'isaiah', 'jeremiah', 'baruch', 'lamentations',
         'epistleofjeremiah', 'ezechiel', 'susanna', 'daniel', 'belandthedragon']

def get_tables():
    """Create Tables"""
    for book in BOOKS:
        make_table(book)

def make_table(book):
    """Make a single Table"""
    Table(f'{book}_lxx', META,
          Column('id', Integer, primary_key=True),
          Column('chapter', Integer),
          Column('verse', Integer),
          Column('text', Text),
          Column('notes', Text))

def execute(engine):
    """Perform migration"""
    get_tables()
    META.create_all(engine)
