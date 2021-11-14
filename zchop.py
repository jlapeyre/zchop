import numpy

_ZCHOP_EPS = 1e-12

def _zchop_real_np(m, eps=_ZCHOP_EPS):
    m[abs(m) < eps] = 0.0
    return m

def zchop(m, eps=_ZCHOP_EPS):
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
