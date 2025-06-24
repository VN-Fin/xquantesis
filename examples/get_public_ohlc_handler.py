
from xno_sdk import OHLCHandler
from xno_sdk import settings


data_handler = OHLCHandler([
    'VN30F1M'
], resolution='m')
data_handler.load_data(from_time='2010-01-01', to_time='2025-06-30')
print(data_handler.get_data())
#
# while True:
#     print(data_handler.get_data())
#     time.sleep(20)
