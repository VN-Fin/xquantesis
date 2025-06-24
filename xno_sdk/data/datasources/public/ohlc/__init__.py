import json
import logging
from datetime import datetime

import requests
from dateutil import parser as date_parser
from tqdm import tqdm
from datetime import UTC as DatetimeUTC

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

    def _stream_request(self, symbol: str, from_ts: int, to_ts: int):
        """
        Prepare the request for streaming OHLC data.
        """
        with requests.get(
                f"{settings.api_base_url}/quant-data/v1/ohlcv",
                headers={"Authorization": f"{settings.api_key}"},
                params={
                    "symbol": symbol,
                    "from": from_ts,
                    "to": to_ts,
                    "resolution": self.resolution,
                },
                stream=True,
        ) as resp:
            resp.raise_for_status()

            for line in resp.iter_lines():  # already decompressed by requests
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as e:
                    logging.error(f"Failed to decode JSON: {e}")
                    continue
                for o, h, l, c, v, t in zip(obj["o"], obj["h"], obj["l"], obj["c"], obj["v"], obj["t"]):
                    yield {
                        "Symbol": symbol,
                        "Time": datetime.fromtimestamp(t, DatetimeUTC).strftime("%Y-%m-%d %H:%M:%S"),
                        "Open": o,
                        "High": h,
                        "Low": l,
                        "Close": c,
                        "Volume": v,
                    }


    def fetch(self, symbols, from_time, to_time, **kwargs):
        self.resolution = kwargs.get("resolution")
        if not self.resolution:
            raise ValueError("resolution=… is required")

        from_ts = int(date_parser.parse(from_time).timestamp())
        to_ts = int(date_parser.parse(to_time).timestamp())

        for symbol in symbols:
            datas = []
            for row in tqdm(self._stream_request(
                    symbol=symbol,
                    from_ts=from_ts,
                    to_ts=to_ts,
            ), desc=f"Fetching {symbol} OHLCV data", unit=" records"):
                datas.append(row)
            if datas:
                logging.debug("Fetched %d rows for %s", len(datas), symbol)
                self.append_df_rows(datas)

    def stream(self, symbols, commit_batch_size, **kwargs):
        pass

