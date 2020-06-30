import math 

def getAs(el, x = 0, z = 0):
    return [[el,  x,  0.25, z],
            [el, 0.5-x, 0.75, z+0.5],
            [el, -x, 0.75, -z],
            [el, x+0.5, 0.25, -z+0.5]]
            
def getBs(el):
    return [[el, 0.0, 0.0, 0.5],
            [el, 0.5, 0.0, 0.0],
            [el, 0.0, 0.5, 0.5],
            [el, 0.5, 0.5, 0.0]]

def getX1s(el, φ = 0):
    x = (math.cos(φ)**2 - 1)/(2 * math.cos(φ)**2 + 4)
    z = (math.sqrt(3) + math.tan(φ)) / math.sqrt(12)
    return [[el,  x,  0.25, z],
            [el, 0.5-x, 0.75, z+0.5-1],
            [el, -x, 0.75, -z+1],
            [el, x+0.5, 0.25, -z+0.5]]
    
def getX2s(el, φ = 0):
    x = (2 - math.sqrt(3)*math.sin(φ)*math.cos(φ)+math.cos(φ)**2) / (8 + 4*math.cos(φ)**2)
    y = - (math.tan(φ)) / math.sqrt(48)
    z = (3*math.sqrt(3) + math.tan(φ)) / math.sqrt(48)
    return [[el, x, y, z],
            [el, 0.5-x, 0.5-y, z+0.5-1],
            [el, -x+1,  y+0.5, -z+1],
            [el, x+0.5, -y, 0.5-z+1],
            [el, -x+1, -y, -z+1],
            [el, -(0.5-x)+1, -(0.5-y)+1, -(z+0.5)+2],
            [el, x, -(y+0.5)+1, z],
            [el, -(x+0.5)+1, y, -(0.5-z)]]

def getSuperCell(A, B, X, φ = 0):
    ret = {"atoms": getAs(A) + getBs(B) + getX1s(X, φ = φ) + getX2s(X, φ = φ)}
    return ret

def getCellVectors(d, φ = 0):
    ret = {
        "a": d/100 * math.sqrt(8 * (2 * math.cos(φ)**2)/3),
        "b": d/100 * math.sqrt(48 / (1 + 2 * (1/math.cos(φ))**2)),
        "c": d/100 * math.sqrt(8) * math.cos(φ)
    }
    return ret
        
    
