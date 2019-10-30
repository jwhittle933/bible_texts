"""Migration Generator"""
import sys
import re
from datetime import datetime

def format_filename(filename):
    """Format Filename
    Split on cap letter, lowercase and join with '_'
    """
    cap_words = re.findall('[A-Z]+[a-z]*', filename)
    return '_'.join([word.lower() for word in cap_words])

if __name__ == "__main__":
    with open(f'database/migrations/{format_filename(sys.argv[1])}_{datetime.now()}.py', 'w+') as f:
        print(f)
        f.write('from sqlalchemy import Table, Column, MetaData\n\n')
        f.write('META = MetaData()\n')
        f.write('def make_table(table_name):\n\t# Make table\n')
        f.write('def alter_table(table_name):\n\t# Alter table\n')
        f.write('def execute_table(table_name):\n\t# Execute table')
