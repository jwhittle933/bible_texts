"""MT Texts migrations"""
from sqlalchemy import Table, Column, Integer, Text, MetaData

META = MetaData()
BOOKS = ['genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy',
         'joshua', 'judges', '1samuel', '2samuel', '1kings', '2kings',
         'isaiah', 'jeremiah', 'ezekiel', 'hosea', 'joel', 'amos', 'obadiah',
         'jonah', 'micah', 'nahum', 'habbakuk', 'zephaniah', 'haggai',
         'zechariah', 'malachi', 'psalms', 'job', 'proverbs', 'ruth',
         'songofsolomon', 'ecclesiastes', 'lamentations', 'esther', 'daniel',
         'ezra', 'nehemiah', 'chronica']

def get_tables():
    """Create Tables"""
    return [make_table(book) for book in BOOKS]

def make_table(book):
    """Make a single Table"""
    return Table(
        f'{book}_mt', META,
        Column('id', Integer, primary_key=True),
        Column('chapter', Integer),
        Column('verse', Integer),
        Column('text', Text),
        Column('notes', Text))

def execute(engine):
    """Perform migration"""
    get_tables()
    META.create_all(engine)
