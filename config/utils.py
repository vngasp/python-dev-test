from calendar import month
from datetime import datetime, timezone
from dateutil.relativedelta import *
import pytz


def get_replace(df, *columns):
   """
   Function that return replace value
   """
   for column in columns:
      df[column] = df[column].astype(str)
      df[column] = df[column].apply(lambda x: x.replace(' ', ''))
      df[column] = df[column].apply(lambda x: x.replace('?', '#ND'))
   return df


def get_remove_nan(df, *columns):
   """
   Function that remove NaN value
   """
   for column in columns:
      df[column] = df[column].fillna(0)
   return df[column]


def get_numeric(df, *columns):
   """
   Function that tranform and return numeric value
   """
   for column in columns:
      df[column] = df[column].apply( lambda x: str(x) )
      df[column] = df[column].apply(lambda x:  int(x) if (x.strip().isnumeric() == True) else 0 )
   return df[column]