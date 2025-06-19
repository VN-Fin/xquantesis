import time

from xno_sdk.data.datasources.internal.ohlc import InternalOhlcDatasource

datasource = InternalOhlcDatasource()

datasource.fetch(
    symbols=["HPG", "VIC", "VHM"],
    from_time="2025-01-01",
    to_time="2025-06-21",
    resolution="m"
)
print(datasource.datas)
datasource._stream(["HPG", "VIC", "VHM"])  # Does not run in background

while True:
    time.sleep(19)
    print(datasource.datas)