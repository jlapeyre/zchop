import copy
import numpy


_ZCHOP_EPS = 1e-12

def _zchop_real_np(m, eps=_ZCHOP_EPS):
    m[abs(m) < eps] = 0.0
    return m

def zchop_mut(m, eps=_ZCHOP_EPS):
    """A mutating version of zchop."""
    if isinstance(m, float):
        if abs(m) < eps:
            return 0.0
        return m
    if isinstance(m, complex):
        return zchop(m.real, eps) + 1j*zchop(m.imag, eps)
    if isinstance(m, list):
        for i, x in enumerate(m):
            m[i] = zchop(x, eps)
        return m
    if isinstance(m, numpy.ndarray):
        if m.dtype == 'float64':
            return _zchop_real_np(m, eps)
        return _zchop_real_np(m.real, eps) + 1j * _zchop_real_np(m.imag, eps)
    if isinstance(m, tuple): # tuple is immutable
        return tuple(zchop(x, eps) for x in m)
    if isinstance(m, int):
        if abs(m) < eps:
            return 0
    return m

def zchop(m, eps=_ZCHOP_EPS):
    """Return a copy of m with small numbers replaced by zero.
    If m is a float, then replace m with 0 if its magnitude is
    less than eps, which is ``1e-12`` by default.
    If m is a complex number, then the real and imaginary parts are
    set to zero or not independently.
    If m is a `list`, `tuple`, or numpy `array`, then the structure is processed
    elementwise and the output type is equal to the input type.
    """
    return zchop_mut(copy.copy(m), eps)
