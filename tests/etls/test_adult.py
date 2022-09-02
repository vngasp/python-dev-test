import pytest
from config.utils import get_datetime
from pandas import DataFrame
from etl.adult import ETL
import datetime as dt
from great_expectations.core.expectation_validation_result import ExpectationSuiteValidationResult


@pytest.fixture
def etl():
    return ETL()


def test_schema(etl):
    df = etl()
    dtypes = {
        'id': 'object',
        'timestamp': 'object',
        'teste': 'object'
    }

    assert type(df) is DataFrame
    assert set(df.columns) == set(list(dtypes.keys()))
    assert dict(df.dtypes) == dtypes


def test_select(etl):
    df = etl()
    df = df.loc[df.id == '']
    assert len(df) == 1
    assert df['timestamp'].item() == '2022-07-06T14:11:01.619'
    assert df['teste'].item() == ''


def test_validation(etl):
    df = etl()
    vr = etl.validate(df)
    assert type(vr) == ExpectationSuiteValidationResult
    assert vr['success'] == True
