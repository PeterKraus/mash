import mendeleev


def _getElMass(elname):
    el = mendeleev.element(elname)
    abu = 0.0
    for iso in el.isotopes:
        if isinstance(iso.abundance, float) and iso.abundance > abu:
            mass = iso.mass
    return mass


def compToXYZ(comp):
    lines = []
    lines.append(f' {len(comp["atoms"])}')
    lines.append(
        f' mash v.{comp["_VER"]:02d}: {comp["tag"]};{comp["a"]:9.6f}x{comp["b"]:9.6f}x{comp["c"]:9.6f};{comp["M"]}-tet; {comp["Glazer"]}'
    )
    for at in comp["atoms"]:
        lines.append(
            f' {at[0]:2s} {at[1]*comp["a"]:9.6f} '
            + f'{at[2]*comp["b"]:9.6f} {at[3]*comp["c"]:9.6f}'
        )
    return lines


def compToCIF(comp):
    lines = []
    lines.append(
        f'# mash v.{comp["_VER"]:02d}: {comp["tag"]};{comp["a"]:9.6f}x{comp["b"]:9.6f}x{comp["c"]:9.6f};{comp["M"]}-tet; {comp["Glazer"]}'
    )
    lines.append(f"data_I")
    lines.append(f'_cell_length_a {comp["a"]:10.7f}')
    lines.append(f'_cell_length_b {comp["b"]:10.7f}')
    lines.append(f'_cell_length_c {comp["c"]:10.7f}')
    lines.append(f'_cell_angle_alpha {comp.get("α", 90):3d}')
    lines.append(f'_cell_angle_beta  {comp.get("β", 90):3d}')
    lines.append(f'_cell_angle_gamma {comp.get("γ", 90):3d}')
    lines.append(f"loop_")
    lines.append(f"    _atom_site_label")
    lines.append(f"    _atom_site_type_symbol")
    lines.append(f"    _atom_site_fract_x")
    lines.append(f"    _atom_site_fract_y")
    lines.append(f"    _atom_site_fract_z")
    lines.append(f"    _atom_site_occupancy")
    for ai in range(len(comp["atoms"])):
        at = comp["atoms"][ai]
        label = f"{at[0]:s}{ai:d}"
        lines.append(
            f"    {label:8s} {at[0]:5s}"
            + f" {at[1]:10.7f} {at[2]:10.7f} {at[3]:10.7f}    1.000"
        )
    return lines


def compToCP2K(comp):
    lines = []
    lines.append(
        f'! mash v.{comp["_VER"]:02d}: {comp["tag"]};{comp["a"]:9.6f}x{comp["b"]:9.6f}x{comp["c"]:9.6f};{comp["M"]}-tet; {comp["Glazer"]}'
    )
    lines.append(f"&GLOBAL")
    lines.append(f'  PROJECT {comp["A"]}{comp["B"]}{comp["X"]}3')
    lines.append(f"  RUN_TYPE CELL_OPT")
    lines.append(f"  PRINT_LEVEL MEDIUM")
    lines.append(f"&END GLOBAL")
    lines.append(f"&FORCE_EVAL")
    lines.append(f"  METHOD Quickstep")
    lines.append(f"  STRESS_TENSOR ANALYTICAL")
    lines.append(f"  &SUBSYS")
    lines.append(f'    &KIND {comp["A"]}')
    lines.append(f'      ELEMENT   {comp["A"]}')
    lines.append(f"      BASIS_SET DZVP-MOLOPT-SR-GTH")
    lines.append(f"      POTENTIAL GTH-PBE")
    lines.append(f"    &END KIND")
    lines.append(f'    &KIND {comp["B"]}')
    lines.append(f'      ELEMENT   {comp["B"]}')
    lines.append(f"      BASIS_SET DZVP-MOLOPT-SR-GTH")
    lines.append(f"      POTENTIAL GTH-PBE")
    lines.append(f"    &END KIND")
    lines.append(f'    &KIND {comp["X"]}')
    lines.append(f'      ELEMENT   {comp["X"]}')
    lines.append(f"      BASIS_SET DZVP-MOLOPT-GTH")
    lines.append(f"      POTENTIAL GTH-PBE")
    lines.append(f"    &END KIND")
    lines.append(f"    &CELL")
    lines.append(f'A {comp["a"]:13.9f} {0.0:13.9f} {0.0:13.9f}')
    lines.append(f'B {0.0:13.9f} {comp["b"]:13.9f} {0.0:13.9f}')
    lines.append(f'C {0.0:13.9f} {0.0:13.9f} {comp["c"]:13.9f}')
    lines.append(f"SYMMETRY ORTHORHOMBIC")
    lines.append(f"    &END CELL")
    lines.append(f"    &COORD")
    lines.append(f"    SCALED T")
    for at in comp["atoms"]:
        lines.append(f"{at[0]:2s} {at[1]:13.9f} {at[2]:13.9f} {at[3]:13.9f}")

    lines.append(f"    &END COORD")
    lines.append(f"  &END SUBSYS")
    lines.append(f"  &DFT")
    if comp["M"] == 1:
        lines.append(f"    UKS FALSE")
    else:
        lines.append(f"    UKS TRUE")
        lines.append(f'    MULTIPLICITY {comp["M"]:2d}')
    lines.append(f"    BASIS_SET_FILE_NAME  BASIS_MOLOPT_UCL")
    lines.append(f"    BASIS_SET_FILE_NAME  BASIS_MOLOPT")
    lines.append(f"    POTENTIAL_FILE_NAME  GTH_POTENTIALS")
    lines.append(f"    &MGRID")
    lines.append(f"      CUTOFF      800")
    lines.append(f"      REL_CUTOFF   90")
    lines.append(f"    &END MGRID")
    lines.append(f"    &XC")
    lines.append(f"      &XC_FUNCTIONAL PBE")
    lines.append(f"      &END XC_FUNCTIONAL")
    lines.append(f"      &XC_GRID")
    lines.append(f"        XC_DERIV      SPLINE3")
    lines.append(f"        XC_SMOOTH_RHO NONE")
    lines.append(f"      &END XC_GRID")
    lines.append(f"      &VDW_POTENTIAL")
    lines.append(f"        POTENTIAL_TYPE PAIR_POTENTIAL")
    lines.append(f"        &PAIR_POTENTIAL")
    lines.append(f"          PARAMETER_FILE_NAME dftd3.dat")
    lines.append(f"          TYPE DFTD3(BJ)")
    lines.append(f"          REFERENCE_FUNCTIONAL PBE")
    lines.append(f"        &END PAIR_POTENTIAL")
    lines.append(f"      &END VDW_POTENTIAL")
    lines.append(f"    &END XC")
    lines.append(f"    &SCF")
    lines.append(f"      SCF_GUESS ATOMIC")
    lines.append(f"      MAX_SCF   200")
    lines.append(f"      EPS_SCF   1.0E-7")
    lines.append(f"      &OT ON")
    lines.append(f"        PRECONDITIONER  FULL_ALL")
    lines.append(f"        MINIMIZER       CG")
    lines.append(f"      &END OT")
    lines.append(f"    &END SCF")
    lines.append(f"    &QS")
    lines.append(f"      EPS_DEFAULT 1.0E-15")
    lines.append(f"    &END QS")
    lines.append(f"  &END DFT")
    lines.append(f"&END FORCE_EVAL")
    lines.append(f"&MOTION")
    lines.append(f"  &GEO_OPT")
    lines.append(f"    TYPE MINIMIZATION")
    lines.append(f"    MAX_FORCE 3.0E-04")
    lines.append(f"    RMS_FORCE 1.0E-03")
    lines.append(f"    MAX_DR    3.0E-04")
    lines.append(f"    RMS_DR    1.0E-03")
    lines.append(f"    MAX_ITER 500")
    lines.append(f"  &END GEO_OPT")
    lines.append(f"  &CELL_OPT")
    lines.append(f"    TYPE DIRECT_CELL_OPT")
    lines.append(f"    PRESSURE_TOLERANCE 10")
    lines.append(f"    KEEP_SYMMETRY TRUE")
    lines.append(f"  &END CELL_OPT")
    lines.append(f"&END MOTION")
    return lines


def compToQE(comp):
    lines = []
    lines.append("&CONTROL")
    lines.append(" CALCULATION_DATA")
    lines.append(f" prefix       = '{comp['A']}{comp['B']}{comp['X']}3',")
    lines.append(" PSEUDO_DATA")
    lines.append(" OUTDIR")
    lines.append("/")
    lines.append("&SYSTEM")
    nkeys = len({"a", "b", "c", "γ"}.intersection(comp.keys()))
    if nkeys == 4:
        lines.append(" ibrav = 12,")
        lines.append(f" A = {comp['a']:13.9f},")
        lines.append(f" B = {comp['b']:13.9f},")
        lines.append(f" C = {comp['c']:13.9f},")
        lines.append(" cosAB = -0.5,")
    elif nkeys == 3:
        lines.append(" ibrav = 8,")
        lines.append(f" A = {comp['a']:13.9f},")
        lines.append(f" B = {comp['b']:13.9f},")
        lines.append(f" C = {comp['c']:13.9f},")
    elif nkeys == 1:
        lines.append(" ibrav = 1,")
        lines.append(f" A = {comp['a']:13.9f},")
    lines.append(f" nat = {len(comp['atoms']):3d},")
    lines.append(" ntyp = 3,")
    lines.append(" ecutwfc = 65.0,")  # SSSP_1.1_efficiency for Mn
    lines.append(" ecutrho = 780.0,")  # SSSP_1.1_efficiency for Mn
    lines.append(" occupations = 'smearing',")
    lines.append(" smearing = 'gauss',")
    lines.append(" degauss = 0.02,")
    lines.append(" FUNCTIONAL_DATA ")
    lines.append(" nspin = 2,")
    lines.append(f" tot_magnetization = {comp['M'] - 1:3d},")
    lines.append("/")
    lines.append("&ELECTRONS")
    lines.append(" mixing_mode = 'plain',")
    lines.append(" mixing_beta = 0.3,")
    lines.append(" startingwfc = 'atomic',")
    lines.append(" conv_thr = 1.0d-8")
    lines.append(" ELECTRON_DATA")
    lines.append("/")
    lines.append("&IONS")
    lines.append(" ion_dynamics = 'bfgs',")
    lines.append("/")
    lines.append("&CELL")
    lines.append(" cell_dynamics = 'bfgs',")
    lines.append(" press_conv_thr = 1,")
    lines.append(" cell_dofree = 'ibrav',")
    lines.append("/")
    lines.append("ATOMIC_SPECIES")
    lines.append(f" {comp['A']:2s} {_getElMass(comp['A']):7.3f} {comp['A']}.upf ")
    lines.append(f" {comp['B']:2s} {_getElMass(comp['B']):7.3f} {comp['B']}.upf ")
    lines.append(f" {comp['X']:2s} {_getElMass(comp['X']):7.3f} {comp['X']}.upf ")
    lines.append("ATOMIC_POSITIONS crystal")
    for at in comp["atoms"]:
        lines.append(f"{at[0]:2s} {at[1]:13.9f} {at[2]:13.9f} {at[3]:13.9f}")
    lines.append("K_POINTS automatic")
    lines.append("3 4 3 0 0 0")
    return lines
