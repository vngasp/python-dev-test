import os
import json

def pytest_sessionstart():
    args = dict()
    args['aws_access_key_id'] = '123'
    args['aws_secret_access_key'] = '456'
    args['database_bonuz_user'] = 'abc'
    args['database_bonuz_pwd'] = 'xyz'
    args['file_zip_pwd'] = 'ghi'
    
    os.environ['args'] = json.dumps(args)
    os.environ['env'] = 'test'