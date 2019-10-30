"""Setup Connection to Database"""
import logging
import yaml
from sqlalchemy import create_engine

LOG = logging.getLogger(__name__)

def get_database(db_type='psql'):
    """Establish connection with db"""
    try:
        engine = get_connection_from_profile(db_type)
        LOG.info("Connected to database")
    except IOError:
        LOG.exception("Failed to connect")
        return None, "failed"

    return engine

def get_connection_from_profile(db_type, config_file_name="./db_config.yaml"):
    """
    Sets up database connection from config file.
    Input:
    config_file_name: YAML file containing databse credentials
                      Top-level keys are psql, mysql, or sqlite

                      Under top-level, HOST, USER,
                      PASSWORD, DATABASE, PORT fields are
                      required
    """
    with open(config_file_name) as f:
        vals = yaml.load(f)
        if db_type not in vals.keys():
            raise Exception(f'Bad config file: no value for {db_type}')

        vals = vals[db_type]
        if not ('HOST' in vals.keys() and
                'USER' in vals.keys() and
                'PASSWORD' in vals.keys() and
                'DATABASE' in vals.keys() and
                'PORT' in vals.keys()):
            req_keys = ['HOST', 'USER', 'PASSWORD', 'DATABASE', 'PORT']
            missing = [val for val in  req_keys if val not in vals[db_type]]
            raise Exception(f'Bad config file: Missing {", ".join(missing)} from required {", ".join(req_keys)}')

    return get_psql_engine(vals['DATABASE'],
                           vals['USER'],
                           vals['HOST'],
                           vals['PORT'],
                           vals['PASSWORD'])

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
    return create_engine(url, pool_size=50, echo=True)
