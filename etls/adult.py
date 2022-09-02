from config.base_etl import Base
from config.source   import Source
from config.target   import Target
from config.config   import Config
from config.utils    import get_replace, get_numeric, get_remove_nan
import great_expectations as ge


class AdultEtl(Base):
    """
    Class AdultEtl
    """

    __table_name__  = 'adult'


    def __init__(self, *args, **kwargs):
        """
        Constructor function of the AdultEtl class
        """
        super(AdultEtl, self).__init__(*args, **kwargs)


    def extract(self):
        """
        Function that extracts datas of database,
        sends a list of extracts to the transform function

        RETURN: Returns a list
        """
        columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
                   'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week',
                   'native-country', 'class']
        return Source(Config).read_csv(columns, 'data/Adult.data')
        


    def transform(self, results):
        """
        Function that turns each extract into a temporary table

        RETURN: Return a list
        """
        get_replace(results, 'workclass', 'education', 'marital-status', 'occupation', 'relationship', 'sex', 'class', 'race', 'native-country')
        get_remove_nan(results, 'age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week')
        get_numeric(results, 'age', 'fnlwgt', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week')
        return results


    def load(self, results):
        """
        Function that saves into a source

        RETURN: Return a list
        """
        Target(Config).sqlite(results, self.__table_name__)


    def validate(self, df):
        if len(df) > 0:
            df = ge.dataset.PandasDataset(df)
            df.expect_column_values_to_not_be_null(column='age')
            df.expect_column_values_to_not_be_null(column='workclass')
            df.expect_column_values_to_not_be_null(column='fnlwgt')
            df.expect_column_values_to_not_be_null(column='education')
            df.expect_column_values_to_not_be_null(column='education-num')
            df.expect_column_values_to_not_be_null(column='marital-status')
            df.expect_column_values_to_not_be_null(column='occupation')
            df.expect_column_values_to_not_be_null(column='relationship')
            df.expect_column_values_to_not_be_null(column='race')
            df.expect_column_values_to_not_be_null(column='sex')
            df.expect_column_values_to_not_be_null(column='capital-gain')
            df.expect_column_values_to_not_be_null(column='capital-loss')
            df.expect_column_values_to_not_be_null(column='hours-per-week')
            df.expect_column_values_to_not_be_null(column='native-country')
            df.expect_column_values_to_not_be_null(column='class')
            return df.validate()