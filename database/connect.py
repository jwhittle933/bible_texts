"""Setup Connection to Database"""
import logging
import yaml
from sqlalchemy import create_engine

LOG = logging.getLogger(__name__)

def get_database():
    """Establish connection with db"""
    try:
        engine = get_connection_from_profile()
        LOG.info("Connected to database")
    except IOError:
        LOG.exception("Failed to connect")
        return None, "failed"

    return engine

def get_connection_from_profile(config_file_name="db_config.yaml"):
    """
    Sets up database connection from config file.
    Input:
    config_file_name: File containing PGHOST, PGUSER,
                      PGPASSWORD, PGDATABASE, PGPORT, which are the
                      credentials for the PostgreSQL database
    """
    with open(config_file_name) as f:
        vals = yaml.load(f)

        if not ('PGHOST' in vals.keys() and
                'PGUSER' in vals.keys() and
                'PGPASSWORD' in vals.keys() and
                'PGDATABASE' in vals.keys() and
                'PGPORT' in vals.keys()):
            raise Exception(f'Bad config file: {config_file_name}')

    return get_psql_engine(vals['PGDATABASE'],
                           vals['PGUSER'],
                           vals['PGHOST'],
                           vals['PGPORT'],
                           vals['PGPASSWORD'])

def get_psql_engine(database, user, host, port, password):
    """
    Get SQLalchemy engine using credentials.
    Input:
    database: database name
    user: Username
    host: Hostname of the database server
    port: Port number
    passwd: Password for the database
    """
    url = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    return create_engine(url, pool_size=50)

def get_creds(vals, db_type='psql'):
    """
    Return correct db creds
    values: psql, mysql, sqlite
    """
    db_creds = vals[db_type]


