import os
import json
from collections import defaultdict

class BaseConfig:
    debug = True

    def __init__(self):
        env = os.environ['env']
        if env == 'prod':
            preset = PRODConfig


class PRODConfig(BaseConfig):
    debug = False

Config = BaseConfig()
