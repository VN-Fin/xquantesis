# xno_sdk/data/handlers/__init__.py
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Union, Any
import pandas as pd

class DataHandler(ABC):
    def __init__(self, symbols: Union[str, List[str]]):
        """
        Initialize the data handler with a list of symbols.
        If a single symbol is provided as a string, it is converted to a list.
        :param symbols:
        """
        if isinstance(symbols, str):
            symbols = [symbols]
        self.symbols = symbols
        self.dataframe: pd.DataFrame = pd.DataFrame()

    @abstractmethod
    def load_data(
        self,
        from_time: Union[str, datetime],
        to_time: Union[str, datetime]
    ) -> pd.DataFrame:
        """
        Load data for the specified time range.
        :param from_time:
        :param to_time:
        :return:
        """

    @abstractmethod
    def stream(self) -> Any:
        """
        Yield / push rows continuously.  Concrete handler decides whether
        this is a generator, async‑generator, or pushes to Redis / WS.
        """
