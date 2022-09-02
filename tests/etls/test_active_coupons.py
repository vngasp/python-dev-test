import pytest
from dataops_etl.utils import get_datetime
from pandas import DataFrame
from dataops_etl.etls.events.active_coupons import ETL
import datetime as dt
from great_expectations.core.expectation_validation_result import ExpectationSuiteValidationResult


@pytest.fixture
def etl():
    return ETL(get_datetime('2022-07-06'), get_datetime('2022-07-07'))


def test_schema(etl):
    df = etl()
    dtypes = {
        'id': 'object',
        'timestamp': 'object',
        'alliance': 'object',
        'sponsor': 'object',
        'experience': 'object',
        'prize': 'object',
        'value': 'float64',
        'amount': 'int64'
    }

    assert type(df) is DataFrame
    assert set(df.columns) == set(list(dtypes.keys()))
    assert dict(df.dtypes) == dtypes


def test_select(etl):
    df = etl()
    df = df.loc[df.id == '633145fbdbf8b4683e846b6226553c01']
    assert len(df) == 1
    assert df['timestamp'].item() == '2022-07-06T14:11:01.619'
    assert df['alliance'].item() == 'vivo'
    assert df['sponsor'].item() == 'bonuz.com'
    assert df['experience'].item() == 'rede-de-protecao-bonus-kafka'
    assert df['prize'].item() == 'bonusCelularVivo'
    assert df['value'].item() == 10.0
    assert df['amount'].item() == 2


def test_validation(etl):
    df = etl()
    vr = etl.validate(df)
    assert type(vr) == ExpectationSuiteValidationResult
    assert vr['success'] == True
