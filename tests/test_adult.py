import pytest
from pandas import DataFrame
from etl.adult import AdultEtl
import datetime as dt
from great_expectations.core.expectation_validation_result import ExpectationSuiteValidationResult


@pytest.fixture
def etl():
    return AdultEtl()


def test_schema(etl):
    df = etl()
    dtypes = {
        'age': 'int64',
        'workclass': 'object',
        'fnlwgt' : 'int64',
        'education' : 'object',
        'education-num' : 'int64',
        'marital-status' : 'object',
        'occupation'    : 'object',
        'relationship'    : 'object',
        'race'  : 'object',
        'sex' : 'object',
        'capital-gain': 'int64',
        'capital-loss' : 'int64',
        'hours-per-week': 'int64',
        'native-country': 'object',
        'class': 'object'
    }
    
    assert type(df) is DataFrame
    assert set(df.columns) == set(list(dtypes.keys()))
    assert dict(df.dtypes) == dtypes


def test_select(etl):
    df = etl()
    df = df.loc[df.age == 25].head(1)
    print(df)
    assert len(df) == 1
    assert df['workclass'].item() == 'Self-emp-not-inc'
    assert df['fnlwgt'].item() == 176756
    assert df['education'].item() == 'HS-grad'
    assert df['education-num'].item() == 9
    assert df['marital-status'].item() == 'Never-married'
    assert df['occupation'].item() == 'Farming-fishing'
    assert df['relationship'].item() == 'Own-child'
    assert df['race'].item() == 'White'
    assert df['sex'].item() == 'Male'
    assert df['capital-gain'].item() == 0
    assert df['capital-loss'].item() == 0
    assert df['hours-per-week'].item() == 35
    assert df['native-country'].item() == 'United-States'
    assert df['class'].item() == '<=50K'


def test_validation(etl):
    df = etl()
    vr = etl.validate(df)
    assert type(vr) == ExpectationSuiteValidationResult
    assert vr['success'] == True
