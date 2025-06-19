import threading
from abc import abstractmethod, ABC
from typing import Union, Iterable, List, Dict, Any

import pandas as pd


class BaseDataSource(ABC):
    _stream_thread: threading.Thread | None = None

    def __init__(self):
        """
        Initialize the base datasource.
        This class should not be instantiated directly.
        """
        self.init_dataframe = False
        self.datas: Union[None, pd.DataFrame] = None
        self.data_buffer: List[dict] = []

    def append_df_rows(self, df: Union[pd.DataFrame, List[Dict[str, Any]]]) -> None:
        """
        Merge *df* into self.datas with (Time, Symbol) uniqueness.
        - For duplicates **within df**: keep the last row.
        - For duplicates vs existing self.datas: last row wins.
        """
        # Normalise input
        if isinstance(df, list):
            df = pd.DataFrame(df)

        df["Time"] = pd.to_datetime(df["Time"])
        df = df.set_index(["Time", "Symbol"])

        # Collapse duplicates INSIDE this chunk
        if not df.index.is_unique:
            df = df[~df.index.duplicated(keep="last")]

        # If main store empty, just assign
        if self.datas.empty:
            self.datas = df
            self.datas.sort_index(level="Time", inplace=True, ascending=True)
            return

        # Overwrite overlapping rows
        overlap_idx = df.index.intersection(self.datas.index)
        if not overlap_idx.empty:
            self.datas.loc[overlap_idx] = df.loc[overlap_idx]

        # Append only brand‑new rows
        new_idx = df.index.difference(self.datas.index)
        if not new_idx.empty:
            self.datas = pd.concat([df.loc[new_idx], self.datas])

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

    def commit_buffer(self):
        """
        Commit the buffered data to the main DataFrame.
        This method can be overridden by subclasses if needed.
        """
        if self.data_buffer:
            df = pd.DataFrame(self.data_buffer)
            self.append_df_rows(df)
            self.data_buffer.clear()
