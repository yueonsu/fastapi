import os
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

env = os.environ['ENV']

DB_USER = '0000'
DB_PASSWORD = '0000'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'test'
if env == 'real':
    DB_HOST = '0000000'
    DB_PORT = '0000'

DB_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

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