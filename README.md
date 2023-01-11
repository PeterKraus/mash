# `mash`: get guess structures of perovskites 

A program for generating guess structures of ABX<sub>3</sub> perovskites. Inspired by `SPuDS` by 
[Lufaso and Woodward](https://doi.org/10.1107/S0108768101015282), but worse - hence `mash`. [Version `1.0`](https://doi.org/10.5281/zenodo.7492808) of this program has been developed by P. Kraus as part of [*Computational workflows for novel materials*](https://doi.org/10.26434/chemrxiv-2023-tjt21) by P. Kraus, P. Raiteri and J. Gale. 

[![Zenodo](https://zenodo.org/badge/DOI/10.5281/zenodo.7492808.svg)](https://doi.org/10.5281/zenodo.7492808)

## Installation

`mash` can be installed via `pip`. `mash` requires `mendeleev`, which can be also installed using `pip`. To install,
clone this repository using `git` and build the package via `pip` using the following command:

```
(mash-test) PS C:\Users\Kraus\Code\mash\test> python -m pip install 'mash @ git+https://github.com/PeterKraus/mash'

 [...]

Successfully built mash
Installing collected packages: [...], mendeleev, mash
Successfully installed [...] mash-1.0.post0.dev6 mendeleev-0.12.1 [...]
```



## Usage

After the above command finished successfully, you can run `mash` using:

```
(mash-test) PS C:\Users\Kraus\Code\mash\test> mash
usage: mash.py [-h] [--otype OTYPE] [--ofile OFILE] [--debug] [--glazer GLAZER] perovskite
mash.py: error: the following arguments are required: perovskite
```

A help command is also available:

```
(mash-test) PS C:\Users\Kraus\Code\mash\test> mash -h
usage: mash [-h] [--otype OTYPE] [--ofile OFILE] [--debug] [--glazer GLAZER] perovskite

positional arguments:
  perovskite       Structural formula of the perovskite to be treated, i.e. [LaMnO3] or [LiMgF3]

optional arguments:
  -h, --help       show this help message and exit
  --otype OTYPE    Output type: [cif, xyz, cp2k, qe]
  --ofile OFILE    Output file prefix
  --debug          Switch logging from info to debug level
  --glazer GLAZER  Request a certain tilt mode: [none, a-a-a-, a+a+a+, a-b+a-]
```


`mash` asks you to provide at least one positional argument: `perovskite`, which is the unit formula (ABX<sub>3</sub>)
of the perovskite that you want to model (e.g. `LaMnO3`). Another important parameter is the `--glazer` switch, which
determines the Glazer tilting system. By default, `--glazer none` is used, which means the program generates a cubic cell
(1 x ABX<sub>3</sub>). `mash` currently supports the following Glazer tilting systems:

- `--glazer a-b+a-`: a<sup>-</sup> b<sup>+</sup> a<sup>-</sup>, generates an orthorhombic cell (4 x ABX<sub>3</sub>)
- `--glazer a-a-a-`: a<sup>-</sup> a<sup>-</sup> a<sup>-</sup>, generates a rhombohedral cell (6 x ABX<sub>3</sub>)
- `--glazer a+a+a+`: a<sup>+</sup> a<sup>+</sup> a<sup>+</sup>, generates a cubic cell (8 x ABX<sub>3</sub>)

