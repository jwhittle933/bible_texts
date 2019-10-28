"""Migration base class"""
import sys
from sqlalchemy import Table, Column, Integer, Text, MetaData


class Migration():
    """Base class for migration
    data and methods"""
    meta = None
    table_name = None
    books = []
    tables = []

    def __init__(self, books, table_name):
        self.meta = MetaData()
        if not isinstance(books, list):
            print("Books must be a list. Received: {books}")
            sys.exit(0)
        self.books = books
        self.table_name = table_name

    def create_tables(self):
        """Create list of tables"""
        self.tables = [self.make_table(book) for book in self.books]
        return self

    def make_table(self, book):
        """Create a single table"""
        return Table(
            book, self.meta,
            Column('id', Integer, primary_key=True),
            Column('chapter', Integer),
            Column('verse', Integer),
            Column('text', Text),
            Column('notes', Text))

    def execute(self, engine):
        """Perform migration"""
        self.meta.create_all(engine)
