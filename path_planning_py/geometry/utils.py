import math

def pointDistance(origin : list, end : list) -> float:
    """Get distance between two points in the 3D space."""
    distance = 0
    if origin != end:
        distance = math.sqrt(
            math.pow(end[0]-origin[0], 2) +
            math.pow(end[1]-origin[1], 2) +
            math.pow(end[2]-origin[2], 2)
        )
    return distance

def normalize(vector : list, reference=[0,0,0]) -> list:
    """Get a normalized vector from a given one. If reference point is
    provided, the vector considered is from the reference to the provided"""
    mag = pointDistance(reference, vector)
    uVector = [
        round((vector[0]-reference[0])/mag, 4),
        round((vector[1]-reference[1])/mag, 4),
        round((vector[2]-reference[2])/mag, 4)
    ]
    return uVector

def movePointDir(point : list, direction : list, distance) -> list:
    """Get a point translated in a direction given by a vector a specified
    amount of distance"""
    dir = normalize(direction)
    newPoint = [
        point[0] + distance * dir[0],
        point[1] + distance * dir[1],
        point[2] + distance * dir[2]
    ]
    return newPoint

def movePointTowards(point : list, target : list, distance) -> list:
    """Get a point translated in a direction defined towards a target point
    a specified amount of distance"""
    direction = normalize(target, point)
    return movePointDir(point, direction, distance)

def crossProduct(u : list, v : list) -> list:
    """Get the vector resulting of cross product of two vectors"""
    w = [
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0]
    ]
    return w

def crossDir(u : list, v : list) -> list:
    """Get unit normal direction of a plane defined by two vectors"""
    return normalize(crossProduct(u,v))

def getRotMatrix(direction : list) -> list:
    """Get u,v,w vectors to determine the rotation matrix of a dextrorotation
    coordinate system with the input of a direction. X axis is considered to
    point forward and Z axis is prioritized to keep upwars"""
    u = normalize(direction)
    if u == [0,1,0]:
        v = crossDir([0,0,1], u)
        w = crossDir(u,v)
    else:
        w = crossDir(u, [0,1,0])
        v = crossDir(w, u)
    return [u,v,w]