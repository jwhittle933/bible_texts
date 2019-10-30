"""Entrypoint module for application"""
import os
import sys
import argparse
from fnmatch import fnmatch
from pathlib import Path
# from migrations.lxx_tables_migrations import execute
from migrations.mt_tables_migrations import execute
from migrations.migration_base import Migration
from connect import get_database

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

def migrate(engine):
    """Perform migrations"""
    execute(engine)

def main(directory='.'):
    """Entrypoint for application"""
    for file in get_files(directory, '*.txt'):
        table_names = os.path.basename(file).replace('.txt', '').lower()
        print(table_names)
        # verses = [Verse(line, 'Proverbs') for line in read_file(file)]
        # verses = [line for line in read_file(file)]
        # for verse in verses:
            # print(verse)
            # insert(verse)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dir',
        type=str,
        default='.')
    parser.add_argument(
        '--migrate',
        type=bool,
        default=False,
        help="""\
        Migrate db tables. This option overrides all others.""")
    parser.add_argument(
        '--db',
        type=str,
        default='psql',
        help="""\
        The database you're using. Accepted values: psql, mysql, sqlite.
        The credentials for your database of choice must be in db_config.yaml,
        and must include: DATABASE, USER, HOST, PORT, PASSWORD""")
    FLAGS, _ = parser.parse_known_args()

    # --migrate overrides all other other options
    if FLAGS.migrate is True:
        print("Migration...")
        ENGINE = get_database(FLAGS.db)
        migrate(ENGINE)
    else:
        print("Main...")
        main(FLAGS.dir)
