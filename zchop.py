import numpy

_ZCHOP_EPS = 1e-12

def _zchop_real_np(m, eps=_ZCHOP_EPS):
    m[abs(m) < eps] = 0.0
    return m

def zchop(m, eps=_ZCHOP_EPS):
    """Replace small numbers in m with zero.
    If m is a float, then replace m with 0 if its magnitude is
    less than eps, which is ``1e-12`` by default.
    If m is a complex number, then the real and imaginary parts are
    set to zero or not independently.
    If m is a `list` or a numpy `array`, then structure is processed
    elementwise and the output type is equal to the input type.
    """
    if isinstance(m, float):
        if abs(m) < eps:
            return 0.0
        return m
    if isinstance(m, complex):
        return zchop(m.real) + 1j*zchop(m.imag)
    if isinstance(m, list):
        return [zchop(x) for x in m]
    if isinstance(m, numpy.ndarray):
        if m.dtype == 'float64':
            return _zchop_real_np(m)
        return _zchop_real_np(m.real) + 1j * _zchop_real_np(m.imag)
    if isinstance(m, int):
        if abs(m) < eps:
            return 0
    return m
