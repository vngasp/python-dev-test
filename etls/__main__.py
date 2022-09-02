import click
import importlib
import os
import json
from datetime import timedelta


@click.command()
@click.argument("etls", nargs=-1)
@click.option("--env",  required=True, type=click.Choice(['test', 'prod']), help="Which environment the project will run?")


def run(etls, env, **options):
    '''
    Run a given ETL with Spark

    ETL is the Class path to run. ex: `datapipeline.etls.etl.AdultEtl`
        Could be multiple ETLs separated with comma.
        ex: datapipeline.etls.etl.AdultEtl, datapipeline.etls.etl.AdultEtlTwo
    '''
    os.environ['args'] = json.dumps(options)
    os.environ['env'] = env

    for etl in etls:
        *path, class_name = etl.split('.')[:]
        path = '.'.join(path)
        job_module = importlib.import_module(path)
        ETL = getattr(job_module, class_name)
        ETL().run_etl()
            

if __name__ == '__main__':
    run()
