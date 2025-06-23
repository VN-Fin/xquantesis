import time

from xno_sdk.data.handlers.ohlc import OHLCHandler
from xno_sdk import settings


data_handler = OHLCHandler([
    'HPG',
    'VIC', 'VHM'
], resolution='m')
data_handler.load_data(from_time='2015-01-01', to_time='2025-06-30')
print(data_handler.get_data())
#
# while True:
#     print(data_handler.get_data())
#     time.sleep(20)
