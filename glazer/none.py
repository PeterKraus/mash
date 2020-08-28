import math
import wyckoff

def getAs(el):
    ret = []
    wpos = wyckoff.positions.Pm3m_221(1, "b", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret
            
def getBs(el):
    ret = []
    wpos = wyckoff.positions.Pm3m_221(1, "a", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret

def getXs(el):
    ret = []
    wpos = wyckoff.positions.Pm3m_221(3, "d", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret
            
    
def getSuperCell(A, B, X, φ = 0):
    ret = {"atoms": getAs(A) + getBs(B) + getXs(X)}
    return ret

def getCellVectors(d, φ = 0):
    ret = {
        "a": d/100,
        "b": d/100,
        "c": d/100
    }
    return ret
