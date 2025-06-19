from typing import List

from sqlalchemy import Connection, text

from xno_sdk.data.datasources import BaseDataSource
import pandas as pd


_BATCH_DAYS = 7           # default “slice” size


class PublicOhlcDatasource(BaseDataSource):
    def fetch(self, symbols, from_time, to_time, **kwargs) -> pd.DataFrame:
        """
        Fetch OHLC data for a given symbol and time range.

        :param symbols: The stock symbol to fetch data for.
        :param from_time: Start time for the data fetch.
        :param to_time: End time for the data fetch.
        :return: DataFrame containing OHLC data.
        """

    def stream(self, symbols, commit_batch_size, **kwargs):
        pass

