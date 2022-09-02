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
            cnx = sqlite3.connect('adult.db')
            df.to_sql(name=table_name, con=cnx)
        return df
