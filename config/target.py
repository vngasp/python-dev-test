from config.config import Config
import sqlite3
from sqlite3 import Error
import pandas as pd


class Target():

    def __init__(self, config):
        self.config = config


    def sqlite(self, df, table_name):
        '''
        Save data to Sqlite
        '''        
        if len(df) > 0:
            cnx = sqlite3.connect(':memory:')
            df.to_sql(name=table_name, con=cnx)
            p1 = pd.read_sql('PRAGMA table_info(adult);', cnx)
            print(p1)
            p2 = pd.read_sql('select * from adult;', cnx)
            print(p2)
        return df
