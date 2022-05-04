import math

def pointDistance(origin : list, end : list) -> float:
    distance = 0
    if origin != end:
        distance = math.sqrt(
            math.pow(end[0]-origin[0], 2) +
            math.pow(end[1]-origin[1], 2) +
            math.pow(end[2]-origin[2], 2)
        )
    return distance

def normalize(vector : list, reference=[0,0,0]) -> list:
    mag = pointDistance(reference, vector)
    uVector = [
        (vector[0]-reference[0])/mag,
        (vector[1]-reference[1])/mag,
        (vector[2]-reference[2])/mag
    ]
    return uVector

def movePointDir(point : list, direction : list, distance) -> list:
    dir = normalize(direction)
    newPoint = [
        point[0] + distance * dir[0],
        point[1] + distance * dir[1],
        point[2] + distance * dir[2]
    ]
    return newPoint

def movePointTowards(point : list, target : list, distance) -> list:
    direction = normalize(target, point)
    return movePointDir(point, direction, distance)

def crossProduct(u : list, v : list) -> list:
    w = [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0]
    ]
    return w

def crossDir(u : list, v : list) -> list:
    return normalize(crossProduct(u,v))

def getRotMatrix(direction : list) -> list:
    u = normalize(direction)
    if u == [0,1,0]:
        v = crossDir([0,0,1], u)
        w = crossDir(u,v)
    else:
        w = crossDir(u, [0,1,0])
        v = crossDir(w, u)
    return [u,v,w]