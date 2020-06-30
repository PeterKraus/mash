import math 

def getA1s(el):
    #return [[el, 0, 0, 0],
    #        [el, 0.5, 0.5, 0.5]]
    return [[el, 0, 0, 0],
            [el, 0.5, 0.5, 0.5]]

def getA2s(el):
    return [[el, 0, 0.5, 0.5],
            [el, 0.5, 0, 0.5],
            [el, 0.5, 0.5, 0],
            [el, 0.5, 0, 0],
            [el, 0, 0.5, 0],
            [el, 0, 0, 0.5]]
            
def getBs(el):
    #return [[el, 0.25, 0.25, 0.25],
    #        [el, 0.25, 0.25, 0.75],
    #        [el, 0.25, 0.75, 0.25],
    #        [el, 0.25, 0.75, 0.75],
    #        [el, 0.75, 0.25, 0.25],
    #        [el, 0.75, 0.25, 0.75],
    #        [el, 0.75, 0.75, 0.25],
    #        [el, 0.75, 0.75, 0.75]]
    return [[el, 0.25, 0.25, 0.25],
            [el, 0.75, 0.75, 0.25],
            [el, 0.75, 0.25, 0.75],
            [el, 0.25, 0.75, 0.75],
            [el, 0.75, 0.75, 0.75],
            [el, 0.25, 0.25, 0.75],
            [el, 0.25, 0.75, 0.25],
            [el, 0.75, 0.25, 0.25]] 

def getXs(el, φ = 0):
    y = (3*math.cos(φ) + math.sqrt(3)*math.sin(φ))/(8 * math.cos(φ) + 4)
    z = (3*math.cos(φ) - math.sqrt(3)*math.sin(φ))/(8 * math.cos(φ) + 4)
    return [[el, 0, y, z],
            [el, 0, 1-y, z],
            [el, 0, y, 1-z],
            [el, 0, 1-y, 1-z],
            [el, z, 0, y],
            [el, z, 0, 1-y],
            [el, 1-z, 0, y],
            [el, 1-z, 0, 1-y],
            [el, y, z, 0],
            [el, 1-y, z, 0],
            [el, y, 1-z, 0],
            [el, 1-y, 1-z, 0],
            [el, 0.5, y+0.5, z+0.5],
            [el, 0.5, -y+0.5, z+0.5],
            [el, 0.5, y+0.5, -z+0.5],
            [el, 0.5, -y+0.5, -z+0.5],
            [el, z+0.5, 0.5, y+0.5],
            [el, z+0.5, 0.5, -y+0.5],
            [el, -z+0.5, 0.5, y+0.5],
            [el, -z+0.5, 0.5, -y+0.5],
            [el, y+0.5, z+0.5, 0.5],
            [el, -y+0.5, z+0.5, 0.5],
            [el, y+0.5, -z+0.5, 0.5],
            [el, -y+0.5, -z+0.5, 0.5]]
            
    

def getSuperCell(A, B, X, φ = 0):
    ret = {"atoms": getA1s(A) + getA2s(A) + getBs(B) + getXs(X, φ = φ)}
    return ret

def getCellVectors(d, φ = 0):
    ret = {
        "a": d/100 * ((8 * math.cos(φ) + 4)/3),
        "b": d/100 * ((8 * math.cos(φ) + 4)/3),
        "c": d/100 * ((8 * math.cos(φ) + 4)/3)
    }
    return ret
