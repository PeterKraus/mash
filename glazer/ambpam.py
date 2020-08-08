import math 
import wyckoff

def getAs(el, x = 0, z = 0):
    ret = []
    wpos = wyckoff.positions.Pnma_62(4, "c", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret
            
def getBs(el):
    ret = []
    wpos = wyckoff.positions.Pnma_62(4, "b", 0, 0, 0)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret

def getX1s(el, φ = 0):
    x = (math.cos(φ)**2 - 1)/(2 * math.cos(φ)**2 + 4)
    z = (math.sqrt(3) + math.tan(φ)) / math.sqrt(12)
    ret = []
    wpos = wyckoff.positions.Pnma_62(4, "c", x, 0, z)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret
    
def getX2s(el, φ = 0):
    x = (2 - math.sqrt(3)*math.sin(φ)*math.cos(φ)+math.cos(φ)**2) / (8 + 4*math.cos(φ)**2)
    y = - (math.tan(φ)) / math.sqrt(48)
    z = (3*math.sqrt(3) + math.tan(φ)) / math.sqrt(48)
    ret = []
    wpos = wyckoff.positions.Pnma_62(8, "d", x, y, z)
    for pos in wpos:
        ret.append([el] + wyckoff.wrap.toCell(pos))
    return ret
    
def getSuperCell(A, B, X, φ = 0):
    ret = {"atoms": getAs(A) + getBs(B) + getX1s(X, φ = φ) + getX2s(X, φ = φ)}
    return ret

def getCellVectors(d, φ = 0):
    ret = {
        "a": d/100 * math.sqrt(8 * (2 + math.cos(φ)**2)/3),
        "b": d/100 * math.sqrt(48 / (1 + 2 * (1/math.cos(φ))**2)),
        "c": d/100 * math.sqrt(8) * math.cos(φ)
    }
    return ret
        
    
