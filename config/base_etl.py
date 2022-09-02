from typing import Dict
from pandas import DataFrame
import traceback
from abc import ABC, abstractmethod
from config.config import Config
from great_expectations.core.expectation_validation_result import (
    ExpectationSuiteValidationResult
)


class Base(ABC):


    @abstractmethod
    def extract(self) -> Dict[str, DataFrame]:
        raise NotImplementedError("method extract not implemented")


    @abstractmethod
    def transform(self, data_sources: Dict[str, DataFrame], table_name) -> DataFrame:
        raise NotImplementedError("method transform not implemented")


    @abstractmethod
    def load(self, df) -> None:
        raise NotImplementedError("method load not implemented")


    @abstractmethod
    def validate(self, df: DataFrame) -> ExpectationSuiteValidationResult:
        raise NotImplementedError("method validate not implemented")


    def run_etl(self) -> DataFrame:

        # extract
        try:
            data_sources = self.extract()
        except Exception:
            self.exception_handler(self.__file_name__, traceback.format_exc(), 'extract')
    
        # transform
        try:
            df = self.transform(data_sources)
        except Exception:
            self.exception_handler(self.__file_name__, traceback.format_exc(), 'transform')

        #load
        try:
            self.load(df)
        except Exception:
            self.exception_handler(self.__file_name__, traceback.format_exc(), 'load')

        return df


    def __call__(self) -> DataFrame:
        df = self.extract()
        df = self.transform(df)
        return df