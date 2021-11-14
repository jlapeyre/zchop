# zchop

This is a python library providing the function `zchop`, which replaces numbers
that are close to zero with zero. `zchop` traverses structures such as `list`s and
numpy `array`s, returning a copy that is the same as the input except that small numbers
are set to zero.

* The parts of complex numbers are treated separately


* Warning. This is an early, not-debugged version.


## Antecedents

This package is based on the Julia pacakge [ZChop.jl](https://github.com/jlapeyre/ZChop.jl), which is in turn based on the
Mathematica function [Chop](https://reference.wolfram.com/language/ref/Chop.html).

