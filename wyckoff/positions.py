
def Pnma_62(multiplicity, letter, x, y, z):
    if multiplicity == 8 and letter == "d":
        return [[x, y, z], [-x + 0.5, -y, z + 0.5],
                [-x, y + 0.5, -z], [x + 0.5, -y + 0.5, -z + 0.5],
                [-x, -y, -z], [x + 0.5, y, -z + 0.5],
                [x, -y + 0.5, z], [-x + 0.5, y + 0.5, z + 0.5]]
    elif multiplicity == 4 and letter == "c":
            return [[x, 0.25, z], [-x + 0.5, 0.75, z + 0.5],
                    [-x, 0.75, -z], [x + 0.5, 0.25, -z + 0.5]]
    elif multiplicity == 4 and letter == "b":
            return [[0.0, 0.0, 0.5], [0.5, 0.0, 0.0],
                    [0.0, 0.5, 0.5], [0.5, 0.5, 0.0]]
    elif multiplicity == 4 and letter == "a":
            return [[0.0, 0.0, 0.0], [0.5, 0.0, 0.5],
                    [0.0, 0.5, 0.0], [0.5, 0.5, 0.5]]
    else:
        raise

def Im3_204(multiplicity, letter, x, y, z):
    if multiplicity == 48 and letter == "h":
        zero = [[x, y, z], [-x, -y, z], [-x, y, -z], [x, -y, -z],
                [z, x, y], [z, -x, -y], [-z, -x, y], [-z, x, -y],
                [y, z, x], [-y, z, -x], [y, -z, -x], [-y, -z, x],
                [-x, -y, -z], [x, y, -z], [x, -y, z], [-x, y, z],
                [-z, -x, -y], [-z, x, y], [z, x, -y], [z, -x, y],
                [-y, -z, -x], [y, -z, x], [-y, z, x], [y, z, -x]]
    elif multiplicity == 24 and letter == "g":
        zero = [[0.0, y, z], [0.0, -y, z], [0.0, y, -z], [0.0, -y, -z],
                [z, 0.0, y], [z, 0.0, -y], [-z, 0.0, y], [-z, 0.0, -y],
                [y, z, 0.0], [-y, z, 0.0], [y, -z, 0.0], [-y, -z, 0.0]]
    elif multiplicity == 16 and letter == "f":
        zero = [[x, x, x], [-x, -x, x], [-x, x, -x], [x, -x, -x],
                [-x, -x, -x], [x, x, -x], [x, -x, x], [-x, x, x]]
    elif multiplicity == 12 and letter == "e":
        zero = [[x, 0.0, 0.5], [-x, 0.0, 0.5], [0.5, x, 0.0],
                [0.5, -x, 0.0], [0.0, 0.5, x], [0.0, 0.5, -x]]
    elif multiplicity == 12 and letter == "d":
        zero = [[x, 0.0, 0.0], [-x, 0.0, 0.0], [0.0, x, 0.0],
                [0.0, -x, 0.0], [0.0, 0.0, x], [0.0, 0.0, -x]]
    elif multiplicity == 8 and letter == "c":
        zero = [[0.25, 0.25, 0.25], [0.75, 0.75, 0.25],
                [0.75, 0.25, 0.75], [0.25, 0.75, 0.75]]
    elif multiplicity == 6 and letter == "b":
        zero = [[0.0, 0.5, 0.5], [0.5, 0.0, 0.5], [0.5, 0.5, 0.0]]
    elif multiplicity == 2 and letter == "a":
        zero = [[0.0, 0.0, 0.0]]

    ret = []
    if zero is not None:
        for i in zero:
            ret.append(i)
            ret.append([i[0] + 0.5, i[1] + 0.5, i[2] + 0.5])
    return ret
    
    
