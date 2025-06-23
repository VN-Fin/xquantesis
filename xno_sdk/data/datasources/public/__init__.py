# xno_sdk/data/datasources/public/__init__.py
import json
import logging
from abc import ABC
import threading
from typing import Iterable, Union, List
from tqdm import tqdm
import pandas as pd
import redis
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy.pool import QueuePool

from xno_sdk.config import RedisConfiguration, DatabaseConfiguration
from xno_sdk.data.datasources import BaseDataSource


class PublicDataSource(BaseDataSource, ABC):
    """
    Shared infrastructure for all public datasources: lazy, process‑wide
    """

    def __init__(self):
        """
        Initialize the internal datasource.
        This class should not be instantiated directly.
        """
        super().__init__()

    def _stream(self, symbols, commit_batch_size=125):
        """
        Stream data from Redis Pub/Sub for the specified symbols.
        :param symbols: List of symbols to subscribe to.
        :param commit_batch_size: Number of messages to buffer before committing.
        """
        pass

    def stream(
        self,
        symbols,
        *,
        commit_batch_size,
        daemon,
        **kwargs,
    ) -> threading.Thread:
        if self._stream_thread and self._stream_thread.is_alive():
            logging.warning("Stream already running")
            return self._stream_thread

        # Build a partial function so we don't leak kwargs
        def _runner():
            self._stream(
                symbols=symbols,
                commit_batch_size=commit_batch_size,
            )

        th = threading.Thread(target=_runner, daemon=daemon, name="OHLC-Stream")
        th.start()
        self._stream_thread = th
        logging.info("Started background stream (%s)", th.name)
        return th
