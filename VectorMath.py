import math

# deprecated
# def limitVectorElements(vector, maxSpeed):
#     vec = ()
#     for x in vector:
#         if x >= maxSpeed:
#             vec += maxSpeed,
#         elif x <= -maxSpeed:
#             vec += -maxSpeed,
#         else:
#             vec += x,
#     return vec

def limit_velocity(boid):
    if abs(boid.velocity[0]) + abs(boid.velocity[1]) > boid.maxVelocity[0] + boid.maxVelocity[1]:
        boid.velocity = [(a/abs(a))*b for a,b in zip(boid.velocity, boid.maxVelocity)]

def calcVec2Distance(pos1, pos2):
    return math.hypot(pos1[0] - pos2[0], pos1[1] - pos2[1])


def addVector2(v1, v2, *args):
    vecList = [v1, v2, *args]
    vec = (0, 0)
    for x in vecList:
        vec = tuple(map(lambda i, j: i + j, vec, x))

    return vec


def subVector2(v1, v2, *args):
    vec = v1
    vecList = [v2, *args]
    for x in vecList:
        vec = tuple(map(lambda i, j: i - j, vec, x))
    return vec
