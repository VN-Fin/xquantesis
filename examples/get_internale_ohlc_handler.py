import time

from xquantesis.data.handlers.ohlc import OHLCHandler
from xquantesis import settings

settings.mode = "internal"  # Set to "public" for public mode

data_handler = OHLCHandler(['HPG', 'VIC', 'VHM'], resolution='D')
data_handler.load_data(from_time='2025-01-01', to_time='2025-06-21').stream()

while True:
    print(data_handler.get_datas())
    time.sleep(20)
