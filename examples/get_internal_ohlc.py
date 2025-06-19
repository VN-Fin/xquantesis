from xno_sdk.data.datasources.internal.ohlc import InternalOhlcDatasource

datasource = InternalOhlcDatasource()

datasource.fetch(
    symbols=["HPG", "VIC"],
    from_time="2025-01-01",
    to_time="2025-06-21",
    resolution="m"
)
datasource.stream(["HPG", "VIC"])

print(datasource.datas)