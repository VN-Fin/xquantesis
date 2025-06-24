import numpy as np

from xno_sdk.timeseries.technicals import ADX

high = np.random.rand(100)
low = np.random.rand(100)
close = np.random.rand(100)

adx = ADX(high, low, close, timeperiod=14)
print(adx)