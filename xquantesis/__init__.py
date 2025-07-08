import os
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'
_log_level = os.environ.get('LOG_LEVEL', 'info').upper()

from .config import settings
from .data.handlers.ohlc import OHLCHandler
import pandas as pd

__all__ = [
    "OHLCHandler",
    "settings",
]
pd.option_context("display.multi_sparse", False)

import logging

logging.basicConfig(
    level=_log_level,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

