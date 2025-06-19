# xno_sdk/data/datasources/internal/ohlc/__init__.py
import pandas as pd
from xno_sdk.data.datasources.internal import InternalDataSource


_query_template = """
SELECT 
    time, symbol, open, high, low, close, volume
FROM trading.stock_ohlcv_history
WHERE (
    symbol = ANY(:symbols) AND resolution = :resolution
    AND time >= :from_time
    AND time < :to_time
)
"""
_yield_records = 5_000
_realtime_topic_template = "data.quant.{symbol}.ohlc"


def data_transform_func(record):
    """
    Transform a record from Redis into a DataFrame row.

    :param record: The record to transform.
    :return: A DataFrame row.
    """
    return {
        "time": record["time"],
        "symbol": record["symbol"],
        "open": record["open"],
        "high": record["high"],
        "low": record["low"],
        "close": record["close"],
        "volume": record["volume"],
    }

class InternalOhlcDatasource(InternalDataSource):
    def __init__(self):
        """
        Initialize the internal OHLC datasource.
        """
        super().__init__()
        self.datas = pd.DataFrame(
            columns=["symbol", "time", "open", "high", "low", "close", "volume"]
        ).set_index(["time", "symbol"]).sort_index()

    def fetch(self, symbols, from_time, to_time, **kwargs):
        """
        Fetch OHLC data for a given symbol and time range using the internal datasource.

        :param symbols: The tickers to fetch data for.
        :param from_time: Start time for the data fetch.
        :param to_time: End time for the data fetch.
        :return: DataFrame containing OHLC data.
        """

        resolution = kwargs.get("resolution", None)
        if resolution is None:
            raise ValueError("Resolution must be specified for fetching OHLC data.")

        for chunk_df in self._query_db(
            query_template=_query_template,
            chunk_size=_yield_records,
            params={
                "symbols": symbols,
                "resolution": resolution,
                "from_time": from_time,
                "to_time": to_time,
            }
        ):
            self.append_df_rows(chunk_df)

    def stream(self, symbols, commit_batch_size=10, **kwargs):
        """
        Stream OHLC data for the specified symbols.
        :param symbols:
        :param commit_batch_size:
        :param kwargs:
        :return:
        """
        self._stream(
            symbols=symbols,
            topic_template=_realtime_topic_template,
            data_transform_func=data_transform_func,
        )
