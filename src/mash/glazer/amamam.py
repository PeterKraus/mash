import math
from .. import wyckoff


def getAs(el):
    ret = []
    wpos = wyckoff.positions.R3c_167(6, "a", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret


def getBs(el):
    ret = []
    wpos = wyckoff.positions.R3c_167(6, "b", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret


def getXs(el, φ=0):
    x = (math.sqrt(3) - math.tan(φ)) / math.sqrt(12)
    ret = []
    wpos = wyckoff.positions.R3c_167(18, "e", x, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret


def getSuperCell(A, B, X, φ=0):
    ret = {"atoms": getAs(A) + getBs(B) + getXs(X, φ=φ)}
    return ret


def getCellVectors(d, φ=0):
    ret = {
        "a": math.sqrt(8) * d / 100 * math.cos(φ),
        "b": math.sqrt(8) * d / 100 * math.cos(φ),
        "c": math.sqrt(48) * d / 100,
        "γ": 120,
    }
    return ret
