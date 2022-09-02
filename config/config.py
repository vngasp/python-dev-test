import os
import json
from collections import defaultdict

class BaseConfig:
    debug = True

    def __init__(self):
        options = json.loads(os.environ['args']) or defaultdict(lambda: None)
        env = os.environ['env']
        self.env = env

        preset = PRODConfig


class PRODConfig(BaseConfig):
    debug = False

Config = BaseConfig()
