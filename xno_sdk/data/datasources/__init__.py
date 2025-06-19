import threading
from abc import abstractmethod, ABC
from typing import Union, Iterable, List

import pandas as pd


class BaseDataSource(ABC):
    _stream_thread: threading.Thread | None = None

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
    def stream(
        self,
        symbols,
        *,
        commit_batch_size,
        daemon,
        **kwargs,
    ) -> threading.Thread:
        """
        Start Redis live stream in a background thread and
        return the Thread object so the caller can `join()`/monitor.

        Parameters
        ----------
        symbols : list[str] | str
        commit_batch_size : int
            Flush `self.data_buffer` into the DataFrame every N messages.
        daemon : bool
            True → thread exits when main program exits.

        Returns
        -------
        threading.Thread
        """
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def data_transform_func(self, record: dict) -> dict:
        raise NotImplementedError()

    def _commit_buffer(self, index_cols: List[str]):
        """
        Commit the buffered data to the main DataFrame.
        This method can be overridden by subclasses if needed.
        """
        if self.data_buffer:
            df = pd.DataFrame(self.data_buffer).set_index(index_cols)
            self.append_df_rows(df)
            self.data_buffer.clear()