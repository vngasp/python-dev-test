from config.config import Config
import pandas as pd
import certifi
import json


class Source():

    def __init__(self, config):
        self.config = config


    def read_csv(self, columns, file_name):
        '''
        Get data from folder from project
        '''
        data = pd.read_csv(file_name, header=None, names=columns)
        data.reset_index(drop=True, inplace=True)
        return data