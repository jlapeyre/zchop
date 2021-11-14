import numpy
from zchop import zchop

def test_scalar():
    assert zchop(1.0) == 1.0
    assert zchop(1e-20) == 0.0

def test_list():
    xin = [1, 2, 1e-15]
    xout = [1, 2, 0]
    assert zchop(xin) == xout

def test_array():
    xin = numpy.array([1, 2, 1e-15])
    xout = numpy.array([1, 2, 0])
    assert numpy.alltrue(zchop(xin) == xout)

def test_complex_array():
    xin = numpy.array([1, 2, 1e-15 + 2.0j])
    xout = numpy.array([1, 2, 2.0j])
    assert numpy.alltrue(zchop(xin) == xout)
