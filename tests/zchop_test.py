import numpy
from zchop import zchop

def test_scalar():
    assert zchop(1.0) == 1.0
    assert zchop(1e-15) == 0.0
    assert zchop(1) == 1
    assert zchop(1, 3) == 0

def test_complex():
    z1 = 1 + 1e-15j
    zz1 = 1 + 0j
    assert zchop(z1) == zz1
    z2 = 1e-15 + 1j
    zz2 = 0.0 + 1j
    assert zchop(z2) == zz2
    za = [z1, z2]
    zza = [zz1, zz2]
    assert zchop(za) == zza
    t = (za, za)
    assert zchop(t) == (zza, zza)
    assert zchop(za + za) == zza + zza

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

def test_hetero():
    assert zchop(["cat", 1e-15]) == ["cat", 0.0]
    assert zchop(["cat", 1e-8]) == ["cat", 1e-8]
    assert zchop(["cat", 1e-8, 1e-15], eps=1e-9) == ["cat", 1e-8, 0.0]
