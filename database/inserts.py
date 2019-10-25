"""Insert Module"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from verse import Verse
from connect import get_database

def insert(verse):
    """Start"""
    db = get_database()
    base = declarative_base()
    Session = sessionmaker(db)
    session = Session()
    base.metadata.create_all(db)

    session.add(verse)
    session.commit()
