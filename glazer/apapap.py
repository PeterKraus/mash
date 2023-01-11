import math
import wyckoff

def getA1s(el):
    ret = []
    wpos = wyckoff.positions.Im3_204(2, "a", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret

def getA2s(el):
    ret = []
    wpos = wyckoff.positions.Im3_204(6, "b", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret
            
def getBs(el):
    ret = []
    wpos = wyckoff.positions.Im3_204(8, "c", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret

def getXs(el, φ = 0):
    y = (3*math.cos(φ) + math.sqrt(3)*math.sin(φ))/(8 * math.cos(φ) + 4)
    z = (3*math.cos(φ) - math.sqrt(3)*math.sin(φ))/(8 * math.cos(φ) + 4)
    ret = []
    wpos = wyckoff.positions.Im3_204(24, "g", 0, y, z)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret
            
    

def getSuperCell(A, B, X, φ = 0):
    ret = {"atoms": getA1s(A) + getA2s(A) + getBs(B) + getXs(X, φ = φ)}
    return ret

def getCellVectors(d, φ = 0):
    ret = {
        "a": d/100 * ((8 * math.cos(φ) + 4)/3)
    }
    return ret
