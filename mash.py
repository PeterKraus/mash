import json
import mendeleev
import math
import os
import argparse
import logging

import export
import glazer

_VERSION = 2

def getRadius(el, charge, coord, mode="only"):
    radii = mendeleev.element(el).ionic_radii
    ret = []
    for r in radii:
        if r.charge == charge and r.coordination == coord:
            ret.append(r)
    if mode == "only":
        assert len(ret) == 1, \
            f'{el}{charge} in {coord}-coordinate is not unique'
        logging.debug(f'Found matching radius for {coord}-coordinate ' + \
                      f'{el}{abs(charge)}{"+" if charge > 0 else "-"}')
        return ret[0]
    if mode == "all" and len(ret) > 0:
        logging.debug(f'Found matching radii for {coord}-coordinate ' + \
                      f'{el}{abs(charge)}{"+" if charge > 0 else "-"}')
        return ret
    logging.warning(f'No matching radius for {coord}-coordinate ' + \
                    f'{el}{abs(charge)}{"+" if charge > 0 else "-"}')
    return []

def getMultiplicity(Ar, Br, cells = 1):
    unpaired = 0
    for r in [Ar, Br]:
        if r.spin == "":
            nel = 0
        elif "d" in r.econf:
            nd = int(r.econf.split("d")[-1])
            if nd <= 3 and r.spin == "HS":
                nel = nd
            elif nd <= 3 and r.spin == "LS":
                raise ValueError(f"What the fuck is this? {el} " + \
                                 f"{charge} {coord}")
            elif nd <= 5 and r.spin == "HS":
                nel = nd
            elif nd <= 6 and r.spin == "LS":
                nel = 3 - (nd - 3)
            elif r.spin == "HS":
                nel = 5 - (nd - 5)
            elif nd <= 8 and r.spin == "LS":
                nel = 2 - (nd - 6)
            elif r.spin == "LS":
                nel = 2 - (nd - 8)
        unpaired += nel * cells
    logging.debug(f"Total supercell multiplicity of {unpaired + 1}")
    return unpaired + 1

def parseArgs():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('perovskite', help=""" Structural formula of the 
                                               perovskite to be treated, i.e.
                                               [LaMnO3] or [LiMgF3] """)
    parser.add_argument('--otype',
                        help="Output type: [cif, xyz, cp2k, qe]",
                        default=False)
    parser.add_argument('--ofile',
                        help="Output file prefix",
                        default=False)
    parser.add_argument('--debug',
                        help="Switch logging from info to debug level", 
                        action='store_const', const=True, default=False)
    parser.add_argument('--glazer',
                        help="Request a certain tilt mode: [none, a-a-a-, a+a+a+, a-b+a-]",
                        default="none")
    
    args = parser.parse_args()
    
    return args 

def deduceABX(name):
    assert name[-1] == "3", \
        f"{name} not in ABX3 format"
    assert sum([1 if i.isupper() else 0 for i in name]) == 3, \
        f"{name} does not have 3 uppercase letters"
        
    initial = dict()
    if name[-2].isupper():
        initial["X"] = name[-2]
        name = name[:-2]
    elif name[-2].islower() and name[-3].isupper():
        initial["X"] = name[-3:-1]
        name = name[:-3]
    logging.debug(f'Initial guess for X: {initial["X"]}')
    if name[1].isupper():
        initial["A"] = name[0]
        name = name[1:]
    elif name[2].isupper():
        initial["A"] = name[:2]
        name = name[2:]
    logging.debug(f'Initial guess for A: {initial["A"]}')
    if len(name) <= 2:
        initial["B"] = name
    else:
        raise ValueError(f'{name} left over')
    logging.debug(f'Initial guess for B: {initial["B"]}')
    return initial
    
def tToφ(t):
    if t < 1.01 and t >= 0.86:
        logging.debug(f"t-factor {t:6.3f} is between 0.86 and 1.0, " + \
                       "φ is reliable")
    else:
        logging.warning(f"t-factor {t:6.3f} is outside 0.86 and 1.0, " + \
                         "φ is unreliable")
        t = max(min(t, 1.0), 0.86)
    return -1.19406040899e9*t**7 \
           +7.70723000557e9*t**6 \
           -2.13128428874e10*t**5 \
           +3.27310528899e10*t**4 \
           -3.01493631049e10*t**3 \
           +1.66569794134e10*t**2 \
           -5.11082473143e9*t \
           +6.71828823777e8

def deduceAnion(name):
    if name in ["O", "S", "Se", "Te"]:
        logging.debug(f'{name} has Q = -2.')
        return -2
    elif name in ["F", "Cl", "Br", "I"]:
        logging.debug(f'{name} has Q = -1.')
        return -1
    else:
        raise ValueError(f'{name} not a common X')

def arTorom(n):
    conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
            [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
            [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
            [   1, 'I']]
    result = ''
    for denom, roman_digit in conv:
        result += roman_digit*(n//denom)
        n %= denom
    return result

def outputHandler(compid, comp, ofile=False, otype=False):
        if ofile:
            fileprefix = f'{ofile}-{compid:02d}'
        else:
            fileprefix = f'{comp["A"]}{comp["B"]}{comp["X"]}3-{compid:02d}'
        logging.debug(f"File prefix set to {fileprefix}")
        if otype in ["xyz", "all"]:
            lines = export.compToXYZ(comp)
            logging.debug(f'Writing {fileprefix+".xyz"}')
            with open(fileprefix + ".xyz", "w") as outfile:
                outfile.write("\n".join(lines))
        if otype in ["cif", "all"]:
            lines = export.compToCIF(comp)
            logging.debug(f'Writing {fileprefix+".cif"}')
            with open(fileprefix + ".cif", "w") as outfile:
                outfile.write("\n".join(lines))
        if otype in ["cp2k", "all"]:
            lines = export.compToCP2K(comp)
            logging.debug(f'Writing {fileprefix+".inp"}')
            with open(fileprefix + ".inp", "w") as outfile:
                outfile.write("\n".join(lines))
        if otype in ["qe", "all"]:
            lines = export.compToQE(comp)
            logging.debug(f'Writing {fileprefix+".qin"}')
            with open(fileprefix + ".qin", "w") as outfile:
                outfile.write("\n".join(lines))
    
def main():
    args = parseArgs()
    logging.basicConfig(level = logging.DEBUG if args.debug else logging.INFO)
    logging.debug(f'Setting logging level to {"DEBUG" if args.debug else "INFO":s}')
    _ABX = deduceABX(args.perovskite)
    _X = {"el": _ABX["X"]}
    _X["r"] = getRadius(_X["el"], deduceAnion(_X["el"]), 'II')
    if _X["r"].charge == -2:
        Qcombs = [[3,3], [2,4], [1,5]]
    else:
        Qcombs = [[1,2]]
    comps = []
    for comb in Qcombs:
        logging.debug(f'Processing composition with charges {comb[0]} and {comb[1]}')
        _B = {"el": _ABX["B"]}
        _B["r"] = getRadius(_B["el"], comb[1], 'VI', mode="all")
        _A = {"el": _ABX["A"]}
        _A["r"] = getRadius(_A["el"], comb[0], 'XII', mode="all")
        if len(_A["r"]) == 0:
            _A["r"] = getRadius(_A["el"], comb[0], 'VIII', mode="all")
        if len(_A["r"]) == 0:
            _A["r"] = getRadius(_A["el"], comb[0], 'VI', mode="all")
        for Br in _B["r"]:
            for Ar in _A["r"]:
                if Ar.ionic_radius > Br.ionic_radius:
                    logging.debug(f'r({_A["el"]}{comb[0]}+) > r({_B["el"]}{comb[1]}+), ' + \
                                  f'creating a composition')
                    comps.append({"A": _A["el"], "B": _B["el"], "X": _X["el"],
                                         "Ar": Ar, "Br": Br, "Xr": _X["r"]})
                else:
                    logging.warning(f'r({_A["el"]}{comb[0]}+) < r({_B["el"]}{comb[1]}+), ' + \
                                  f'try revering input')
                                  
    logging.debug('Filtering compositions based on τ:')
    for comp in comps:
        comp["Glazer"] = args.glazer
        comp["tag"] = f'{comp["A"]}({arTorom(abs(comp["Ar"].charge))}+)' + \
                      f'{comp["B"]}({arTorom(abs(comp["Br"].charge))}+)' + \
                      f'({comp["X"]}({arTorom(abs(comp["Xr"].charge))}-))3'
        comp["_VER"] = _VERSION
        logging.debug(f'Candidate {comp["tag"]}')
        
        comp["τ"] = comp["Xr"].ionic_radius / comp["Br"].ionic_radius \
                    - comp["Ar"].charge * (comp["Ar"].charge \
                    - (comp["Ar"].ionic_radius/comp["Br"].ionic_radius) / \
                    math.log(comp["Ar"].ionic_radius/comp["Br"].ionic_radius))
        if comp["τ"] < 4.18:
            logging.debug(f'With τ = {comp["τ"]:5.3f}, ' + \
                           'this could be a perovskite')
        else:
            logging.warning(f'With τ = {comp["τ"]:5.3f}, ' + \
                             'this is not likely a perovskite')
            continue
        comp["t"] = (comp["Ar"].ionic_radius + comp["Xr"].ionic_radius) / \
                    (math.sqrt(2) * (comp["Br"].ionic_radius + comp["Xr"].ionic_radius))
        comp["φ°"] = tToφ(comp["t"])
        comp["φ"] = math.radians(comp["φ°"])
        comp["d"] = comp["Br"].ionic_radius + comp["Xr"].ionic_radius
        
        if args.glazer == "none":
            celltype = "cubic"
            comp["φ"] = 0
            gls = glazer.none
            ncells = 1
        elif args.glazer == "a-a-a-":
            celltype = "rhombohedral"
            gls = glazer.amamam
            ncells = 6
        elif args.glazer == "a+a+a+":
            celltype = "cubic"
            gls = glazer.apapap
            ncells = 8
        elif args.glazer == "a-b+a-":
            celltype = "orthorhombic"
            gls = glazer.ambpam
            ncells = 4
        
        comp["M"] = getMultiplicity(comp["Ar"], comp["Br"], cells = ncells)
        
        logging.debug(f"Assuming {celltype} supercell with {args.glazer} tilting")
        comp.update(gls.getCellVectors(comp["d"], φ = comp["φ"]))
        comp.update(gls.getSuperCell(comp["A"], comp["B"], comp["X"],
                                     φ = comp["φ"]))
        outputHandler(comps.index(comp), comp,
                      ofile = args.ofile, otype = args.otype)
        
if __name__ == "__main__":
    main()
