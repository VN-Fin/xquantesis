
from xno_sdk import OHLCHandler
from xno_sdk import settings
import time

#
# or
# settings.api_key = 'your_api_key_here'  # Replace with your actual API key


data_handler = OHLCHandler([
    'VN30F1M', 'VN30F2M'
], resolution='m')
data_handler.load_data(from_time='2025-07-01', to_time='2025-12-31').stream()
print(data_handler.get_datas())
#
while True:
    print("Current DataFrame:")
    print(data_handler.get_datas())
    print("Data for VN30F1M:")
    print(data_handler.get_data('VN30F1M'))
    time.sleep(20)
