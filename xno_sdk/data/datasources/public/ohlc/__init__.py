import json
import logging
from datetime import datetime

import requests
from dateutil import parser as date_parser
from tqdm import tqdm

from xno_sdk import settings
import pandas as pd

from xno_sdk.data.datasources.public import PublicDataSource


class PublicOhlcDatasource(PublicDataSource):
    def data_transform_func(self, record: dict) -> dict:
        pass

    def __init__(self):
        """
        Initialize the internal OHLC datasource.
        """
        super().__init__()
        self.datas = pd.DataFrame(
            columns=["Symbol", "Time", "Open", "High", "Low", "Close", "Volume"]
        ).set_index(["Time", "Symbol"])
        self.resolution = None  # Placeholder for resolution, to be set during fetch

    def fetch(self, symbols, from_time, to_time, **kwargs):
        """
        Fetch OHLC data for a given symbol and time range.

        :param symbols: The stock symbol to fetch data for.
        :param from_time: Start time for the data fetch.
        :param to_time: End time for the data fetch.
        """
        self.resolution = kwargs.get("resolution", None)
        if self.resolution is None:
            raise ValueError("Resolution must be specified for fetching OHLC data.")

        from_time = int(date_parser.parse(from_time).timestamp())
        to_time = int(date_parser.parse(to_time).timestamp())
        for symbol in symbols:
            logging.debug(f"Fetching OHLCV data for {symbol} from {from_time} to {to_time}")
            response = requests.get(
                settings.api_base_url + "/quant-data/v1/ohlcv",
                headers={'Authorization': f"Bearer {settings.api_key}"},
                params={
                    'symbol': symbol,
                    'from': int(from_time),  # match the API query param
                    'to': int(to_time),
                    'resolution': self.resolution
                },
                stream=True
            )
            if response.status_code != 200:
                logging.warning(f"Failed to fetch data for {symbol}: {response.status_code} {response.text}")
                continue

            datas = []
            for line in tqdm(response.iter_lines(), desc=f"Fetching OHLCV {symbol} ({self.resolution})"):
                if not line:
                    continue
                obj = json.loads(line)
                # Construct datas from response object
                datas.extend([
                    {
                        "Symbol": symbol,
                        "Time": datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"),
                        "Open": o,
                        "High": h,
                        "Low": l,
                        "Close": c,
                        "Volume": v
                    } for o, h, l, c, v, t in zip(obj['o'], obj['h'], obj['l'], obj['c'], obj['v'], obj['t'])
                ])

            if datas:
                logging.info(f"Fetched {len(datas)} records for {symbol} from {from_time} to {to_time}")
                self.append_df_rows(datas)

    def stream(self, symbols, commit_batch_size, **kwargs):
        pass

