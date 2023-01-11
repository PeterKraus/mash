def Pnma_62(multiplicity, letter, x, y, z):
    if multiplicity == 8 and letter == "d":
        return [
            [ x, y,     z], [-x+0.5,-y,     z+0.5],  # fmt: skip
            [-x, y+0.5,-z], [ x+0.5,-y+0.5,-z+0.5],  # fmt: skip
            [-x,-y,    -z], [ x+0.5, y,    -z+0.5],  # fmt: skip
            [ x,-y+0.5, z], [-x+0.5, y+0.5, z+0.5],  # fmt: skip
        ]
    elif multiplicity == 4 and letter == "c":
        return [
            [ x,0.25, z], [-x+0.5,0.75, z+0.5],  # fmt: skip
            [-x,0.75,-z], [ x+0.5,0.25,-z+0.5],  # fmt: skip
        ]
    elif multiplicity == 4 and letter == "b":
        return [
            [0.0,0.0,0.5], [0.5,0.0,0.0],  # fmt: skip
            [0.0,0.5,0.5], [0.5,0.5,0.0],  # fmt: skip
        ]
    elif multiplicity == 4 and letter == "a":
        return [
            [0.0,0.0,0.0], [0.5,0.0,0.5],  # fmt: skip
            [0.0,0.5,0.0], [0.5,0.5,0.5],  # fmt: skip
        ]
    else:
        raise


def Im3_204(multiplicity, letter, x, y, z):
    if multiplicity == 48 and letter == "h":
        zero = [
            [ x, y, z], [-x,-y, z], [-x, y,-z], [ x,-y,-z],  # fmt: skip
            [ z, x, y], [ z,-x,-y], [-z,-x, y], [-z, x,-y],  # fmt: skip
            [ y, z, x], [-y, z,-x], [ y,-z,-x], [-y,-z, x],  # fmt: skip
            [-x,-y,-z], [ x, y,-z], [ x,-y, z], [-x, y, z],  # fmt: skip
            [-z,-x,-y], [-z, x, y], [ z, x,-y], [ z,-x, y],  # fmt: skip
            [-y,-z,-x], [ y,-z, x], [-y, z, x], [ y, z,-x],  # fmt: skip
        ]
    elif multiplicity == 24 and letter == "g":
        zero = [
            [0.0,  y,  z], [0.0, -y,  z], [0.0,  y, -z], [0.0, -y, -z],  # fmt: skip
            [  z,0.0,  y], [  z,0.0, -y], [ -z,0.0,  y], [ -z,0.0, -y],  # fmt: skip
            [  y,  z,0.0], [ -y,  z,0.0], [  y, -z,0.0], [ -y, -z,0.0],  # fmt: skip
        ]
    elif multiplicity == 16 and letter == "f":
        zero = [
            [ x, x, x], [-x,-x, x], [-x, x,-x], [ x,-x,-x],  # fmt: skip
            [-x,-x,-x], [ x, x,-x], [ x,-x, x], [-x, x, x],  # fmt: skip
        ]
    elif multiplicity == 12 and letter == "e":
        zero = [
            [  x,0.0,0.5], [ -x,0.0,0.5], [0.5,  x,0.0],  # fmt: skip
            [0.5, -x,0.0], [0.0,0.5,  x], [0.0,0.5, -x],  # fmt: skip
        ]
    elif multiplicity == 12 and letter == "d":
        zero = [
            [  x,0.0,0.0], [ -x,0.0,0.0], [0.0,  x,0.0],  # fmt: skip
            [0.0, -x,0.0], [0.0,0.0,  x], [0.0,0.0, -x],  # fmt: skip
        ]
    elif multiplicity == 8 and letter == "c":
        zero = [
            [0.25,0.25,0.25], [0.75,0.75,0.25],  # fmt: skip
            [0.75,0.25,0.75], [0.25,0.75,0.75],  # fmt: skip
        ]
    elif multiplicity == 6 and letter == "b":
        zero = [[0.0,0.5,0.5], [0.5,0.0,0.5], [0.5,0.5,0.0]]  # fmt: skip
    elif multiplicity == 2 and letter == "a":
        zero = [[0.0,0.0,0.0]]  # fmt: skip

    ret = []
    if zero is not None:
        for i in zero:
            ret.append(i)
            ret.append([i[0] + 0.5, i[1] + 0.5, i[2] + 0.5])
    return ret


def R3c_167(multiplicity, letter, x, y, z):
    if multiplicity == 36 and letter == "f":
        zero = [
            [  x, y,     z], [-y, x-y,     z], [-x+y,-x,    z], [y,   x,-z+0.5],  # fmt: skip
            [x-y,-y,-z+0.5], [-x,-x+y,-z+0.5], [  -x,-y,   -z], [y,-x+y,    -z],  # fmt: skip
            [x-y, x,    -z], [-y,  -x, z+0.5], [-x+y, y,z+0.5], [x, x-y, z+0.5],  # fmt: skip
        ]
    elif multiplicity == 18 and letter == "e":
        zero = [
            [ x,0.0,0.25], [0.0, x,0.25], [-x,-x,0.25],  # fmt: skip
            [-x,0.0,0.75], [0.0,-x,0.75], [ x, x,0.75],  # fmt: skip
        ]
    elif multiplicity == 18 and letter == "d":
        zero = [
            [0.5,0.0,0.0], [0.0,0.5,0.0],  # fmt: skip
            [0.5,0.5,0.0], [0.0,0.5,0.5],  # fmt: skip
            [0.5,0.0,0.5], [0.5,0.5,0.5],  # fmt: skip
        ]
    elif multiplicity == 12 and letter == "c":
        zero = [
            [0.0,0.0, z], [0.0,0.0,-z+0.5],  # fmt: skip
            [0.0,0.0,-z], [0.0,0.0, z+0.5],  # fmt: skip
        ]
    elif multiplicity == 6 and letter == "b":
        zero = [[0.0,0.0,0.0], [0.0,0.0,0.5]]  # fmt: skip
    elif multiplicity == 6 and letter == "a":
        zero = [[0.0,0.0,0.25], [0.0,0.0,0.75]]  # fmt: skip

    ret = []
    if zero is not None:
        for i in zero:
            ret.append(i)
            ret.append([i[0] + 2.0 / 3.0, i[1] + 1.0 / 3.0, i[2] + 1.0 / 3.0])
            ret.append([i[0] + 1.0 / 3.0, i[1] + 2.0 / 3.0, i[2] + 2.0 / 3.0])
    return ret


def Pm3m_221(multiplicity, letter, x, y, z):
    if multiplicity == 48 and letter == "n":
        return [
            [x,y,z], [-x,-y,z], [-x,y,-z], [x,-y,-z],  # fmt: skip
            [z,x,y], [z,-x,-y], [-z,-x,y], [-z,x,-y],  # fmt: skip
            [y,z,x], [-y,z,-x], [y,-z,-x], [-y,-z,x],  # fmt: skip
            [y,x,-z], [-y,-x,-z], [y,-x,z], [-y,x,z],  # fmt: skip
            [x,z,-y], [-x,z,y], [-x,-z,-y], [x,-z,y],  # fmt: skip
            [z,y,-x], [z,-y,x], [-z,y,x], [-z,-y,-x],  # fmt: skip
            [-x,-y,-z], [x,y,-z], [x,-y,z], [-x,y,z],  # fmt: skip
            [-z,-x,-y], [-z,x,y], [z,x,-y], [z,-x,y],  # fmt: skip
            [-y,-z,-x], [y,-z,x], [-y,z,x], [y,z,-x],  # fmt: skip
            [-y,-x,z], [y,x,z], [-y,x,-z], [y,-x,-z],  # fmt: skip
            [-x,-z,y], [x,-z,-y], [x,z,y], [-x,z,-y],  # fmt: skip
            [-z,-y,x], [-z,y,-x], [z,-y,-x], [z,y,x],  # fmt: skip
        ]
    elif multiplicity == 24 and letter == "m":
        return [
            [x,x,z], [-x,-x,z], [-x,x,-z], [x,-x,-z],  # fmt: skip
            [z,x,x], [z,-x,-x], [-z,-x,x], [-z,x,-x],  # fmt: skip
            [x,z,x], [-x,z,-x], [x,-z,-x], [-x,-z,x],  # fmt: skip
            [x,x,-z], [-x,-x,-z], [x,-x,z], [-x,x,z],  # fmt: skip
            [x,z,-x], [-x,z,x], [-x,-z,-x], [x,-z,x],  # fmt: skip
            [z,x,-x], [z,-x,x], [-z,x,x], [-z,-x,-x],  # fmt: skip
        ]
    elif multiplicity == 24 and letter == "l":
        return [
            [0.5,y,z], [0.5,-y,z], [0.5,y,-z], [0.5,-y,-z],  # fmt: skip
            [z,0.5,y], [z,0.5,-y], [-z,0.5,y], [-z,0.5,-y],  # fmt: skip
            [y,z,0.5], [-y,z,0.5], [y,-z,0.5], [-y,-z,0.5],  # fmt: skip
            [y,0.5,-z], [-y,0.5,-z], [y,0.5,z], [-y,0.5,z],  # fmt: skip
            [0.5,z,-y], [0.5,z,y], [0.5,-z,-y], [0.5,-z,y],  # fmt: skip
            [z,y,0.5], [z,-y,0.5], [-z,y,0.5], [-z,-y,0.5],  # fmt: skip
        ]
    elif multiplicity == 24 and letter == "l":
        return [
            [0.0,y,z], [0.0,-y,z], [0.0,y,-z], [0.0,-y,-z],  # fmt: skip
            [z,0.0,y], [z,0.0,-y], [-z,0.0,y], [-z,0.0,-y],  # fmt: skip
            [y,z,0.0], [-y,z,0.0], [y,-z,0.0], [-y,-z,0.0],  # fmt: skip
            [y,0.0,-z], [-y,0.0,-z], [y,0.0,z], [-y,0.0,z],  # fmt: skip
            [0.0,z,-y], [0.0,z,y], [0.0,-z,-y], [0.0,-z,y],  # fmt: skip
            [z,y,0.0], [z,-y,0.0], [-z,y,0.0], [-z,-y,0.0],  # fmt: skip
        ]
    elif multiplicity == 12 and letter == "j":
        return [
            [0.5,y,y], [0.5,-y,y], [0.5,y,-y], [0.5,-y,-y],  # fmt: skip
            [y,0.5,y], [y,0.5,-y], [-y,0.5,y], [-y,0.5,-y],  # fmt: skip
            [y,y,0.5], [-y,y,0.5], [y,-y,0.5], [-y,-y,0.5],  # fmt: skip
        ]
    elif multiplicity == 12 and letter == "i":
        return [
            [0.0,y,y], [0.0,-y,y], [0.0,y,-y], [0.0,-y,-y],  # fmt: skip
            [y,0.0,y], [y,0.0,-y], [-y,0.0,y], [-y,0.0,-y],  # fmt: skip
            [y,y,0.0], [-y,y,0.0], [y,-y,0.0], [-y,-y,0.0],  # fmt: skip
        ]
    elif multiplicity == 12 and letter == "h":
        return [
            [  x,0.5,0.0], [ -x,0.5,0.0], [0.0,  x,0.5], [0.0, -x,0.5],  # fmt: skip
            [0.5,0.0,  x], [0.5,0.0, -x], [0.5,  x,0.0], [0.5, -x,0.0],  # fmt: skip
            [  x,0.0,0.5], [ -x,0.0,0.5], [0.0,0.5, -x], [0.0,0.5,  x],  # fmt: skip
        ]
    elif multiplicity == 8 and letter == "g":
        return [
            [x,x,x], [-x,-x,x], [-x,x,-x], [x,-x,-x],  # fmt: skip
            [x,x,-x], [-x,-x,-x], [x,-x,x], [-x,x,x],  # fmt: skip
        ]
    elif multiplicity == 6 and letter == "f":
        return [
            [  x,0.5,0.5], [ -x,0.5,0.5], [0.5,  x,0.5],  # fmt: skip
            [0.5, -x,0.5], [0.5,0.5,  x], [0.5,0.5, -x],  # fmt: skip
        ]
    elif multiplicity == 6 and letter == "e":
        return [
            [  x,0.0,0.0], [ -x,0.0,0.0], [0.0,  x,0.0],  # fmt: skip
            [0.0, -x,0.0], [0.0,0.0,  x], [0.0,0.0, -x],  # fmt: skip
        ]
    elif multiplicity == 3 and letter == "d":
        return [[0.5,0.0,0.0], [0.0,0.5,0.0], [0.0,0.0,0.5]]  # fmt: skip
    elif multiplicity == 3 and letter == "c":
        return [[0.0,0.5,0.5], [0.5,0.0,0.5], [0.5,0.5,0.0]]  # fmt: skip
    elif multiplicity == 1 and letter == "b":
        return [[0.5,0.5,0.5]]  # fmt: skip
    elif multiplicity == 1 and letter == "a":
        return [[0.0,0.0,0.0]]  # fmt: skip
    else:
        raise
