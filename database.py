import os
import sqlalchemy
import configparser

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

env = os.environ['ENV']
config = configparser.ConfigParser()
db_config = 'real.ini' if env == 'real' else 'local.ini'
config.read('dbconfig-' + db_config)

DB_URL = sqlalchemy.engine.URL.create(
    drivername='mysql+pymysql',
    username=config['WORKSPACEDB']['USER'],
    password=config['WORKSPACEDB']['PASSWORD'],
    host=config['WORKSPACEDB']['HOST'],
    port=config['WORKSPACEDB']['PORT'],
    database=config['WORKSPACEDB']['DATABASE']
)

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn