from abc import abstractmethod

from xno_sdk import settings
from xno_sdk.data.datasources.internal.ohlc import InternalOhlcDatasource
from xno_sdk.data.datasources.public.ohlc import PublicOhlcDatasource
from xno_sdk.data.handlers import DataHandler


class OHLCHandler(DataHandler):
    def __init__(self, symbols, resolution):
        super().__init__(symbols)
        self.resolution = resolution
        self.source = PublicOhlcDatasource if settings.mode == "public" else InternalOhlcDatasource()

    def load_data(self, from_time, to_time):
        df = self.source.fetch(self.symbols, from_time, to_time, resolution=self.resolution)
        return df

    def stream(self):
        return self.source.stream(self.symbols, resolution=self.resolution)