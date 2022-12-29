# `mash` version 1.0
A program for generating guess structures of ABX<sub>3</sub> perovskites. Inspired by `SPuDS` by Lufaso and Woodward, 
[[1]](https://doi.org/10.1107/S0108768101015282) but worse - hence `mash`. This program has been developed by P. Kraus as part of *Computational workflows for novel materials* by P. Kraus, P. Raiteri and J. Gale.

## Installation

`mash` requires `mendeleev`, which can be installed using `pip`. Other than that, clone this repository, and run
`mash` using `python mash.py`, which should print usage information:

## Usage

```
(mash-dev) PS C:\Users\Kraus\Code\mash> python .\mash.py
usage: mash.py [-h] [--otype OTYPE] [--ofile OFILE] [--debug] [--glazer GLAZER] perovskite
mash.py: error: the following arguments are required: perovskite
```

`mash` asks you to provide at least one positional argument: `perovskite`, which is the unit formula (ABX<sub>3</sub>)
of the perovskite that you want to model (e.g. `LaMnO3`). Another important parameter is the `--glazer` switch, which
determines the Glazer tilting system. By default, `--glazer none` is used, which means the program generates a cubic cell
(1 x ABX<sub>3</sub>). `mash` currently supports the following Glazer tilting systems:

- `--glazer a-b+a-`: a<sup>-</sup> b<sup>+</sup> a<sup>-</sup>, generates an orthorhombic cell (4 x ABX<sub>3</sub>)
- `--glazer a-a-a-`: a<sup>-</sup> a<sup>-</sup> a<sup>-</sup>, generates a rhombohedral cell (6 x ABX<sub>3</sub>)
- `--glazer a+a+a+`: a<sup>+</sup> a<sup>+</sup> a<sup>+</sup>, generates a cubic cell (8 x ABX<sub>3</sub>)

