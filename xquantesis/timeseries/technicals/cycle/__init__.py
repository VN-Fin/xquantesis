from xquantesis.timeseries._internal import _call_func


@_call_func
def HT_DCPERIOD(real):
    """
    Hilbert Transform - Dominant Cycle Period.

    Calculates the dominant cycle period using the Hilbert Transform.

    :param real: array-like
        Array of input data (e.g., closing prices).

    :return: numpy.ndarray
        Dominant cycle period values.
    """
    pass

@_call_func
def HT_DCPHASE(real):
    """
    Hilbert Transform - Dominant Cycle Phase.

    Calculates the dominant cycle phase using the Hilbert Transform.

    :param real: array-like
        Array of closing prices.

    :return: numpy.ndarray
        Dominant cycle phase values.
    """

@_call_func
def HT_PHASOR(real):
    """
    Hilbert Transform - Phasor Components.

    Calculates the phasor components using the Hilbert Transform.

    :param real: array-like
        Array of input data (e.g., closing prices).

    :return: tuple of numpy.ndarray
        (inphase, quadrature)
        - inphase: In-phase component values.
        - quadrature: Quadrature component values.
    """
    pass

@_call_func
def HT_SINE(real):
    """
    Hilbert Transform - Sine Wave.

    Calculates the sine wave components using the Hilbert Transform.

    :param real: array-like
        Array of input data (e.g., closing prices).

    :return: tuple of numpy.ndarray
        (sine, leadsine)
        - sine: Sine component values.
        - leadsine: Lead sine component values.
    """
    pass

@_call_func
def HT_TRENDMODE(real):
    """
    Hilbert Transform - Trend vs Cycle Mode.

    Determines whether the data is in trend or cycle mode using the Hilbert Transform.

    :param real: array-like
        Array of input data (e.g., closing prices).

    :return: numpy.ndarray
        Trend vs Cycle mode values.
    """
    pass
