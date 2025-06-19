from abc import abstractmethod, ABC
from typing import Union, Iterable, List

import pandas as pd


class BaseDataSource(ABC):
    def __init__(self):
        """
        Initialize the base datasource.
        This class should not be instantiated directly.
        """
        self.datas: Union[None, pd.DataFrame] = None
        self.data_buffer: List[dict] = []

    def append_df_rows(self, df: pd.DataFrame) -> None:
        """rows → list[dict] with keys matching the columns."""
        self.datas = pd.concat([self.datas, df])

    @abstractmethod
    def fetch(self, symbols, from_time, to_time, *args, **kwargs) -> pd.DataFrame:
        """
        Fetch data from the datasource.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def stream(self, symbols, *args, **kwargs):
        """
        Stream data from the datasource.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def _commit_buffer(self, index_cols: List[str]):
        """
        Commit the buffered data to the main DataFrame.
        This method can be overridden by subclasses if needed.
        """
        if self.data_buffer:
            df = pd.DataFrame(self.data_buffer).set_index(index_cols)
            self.append_df_rows(df)
            self.data_buffer.clear()