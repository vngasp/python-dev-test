import os
import json

def pytest_sessionstart():
    os.environ['env'] = 'test'