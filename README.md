# mash
A program for generating guess structures of ABX<sub>3</sub> perovskites. Inspired by SPuDS by Lufaso and Woodward, 
[[1]](https://doi.org/10.1107/S0108768101015282) but worse - hence `mash`.

Currently supports the following Glazer tilting systems:
- none: generates a cubic cell (1 x ABX<sub>3</sub>)
- a<sup>-</sup> b<sup>+</sup> a<sup>-</sup>: generates an orthorhombic cell (4 x ABX<sub>3</sub>)
- a<sup>-</sup> a<sup>-</sup> a<sup>-</sup>: generates a rhombohedral cell (6 x ABX<sub>3</sub>)
- a<sup>+</sup> a<sup>+</sup> a<sup>+</sup>: generates a cubic cell (8 x ABX<sub>3</sub>)
