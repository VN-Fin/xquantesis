import numpy as np
import xno_sdk.timeseries as ts

open_ = np.random.rand(100)
high = np.random.rand(100)
low = np.random.rand(100)
close = np.random.rand(100)
volume = np.random.rand(100)

adx = ts.ADX(high, low, close, timeperiod=14)
print("ADX:", adx)