import VectorMath as vm


def coherence(centerBoidPosition, visibleBoids, coherenceFactor):
    # Calculate the center position of all "visible" boids except this one, calculate direction vector
    # towards that point and scale it by the coherence factor. Then return it
    perceivedCenter = (0, 0)
    for boid in visibleBoids:
        perceivedCenter = vm.addVector2(perceivedCenter, boid.position)
    if len(visibleBoids) > 1:
        perceivedCenter = (x / len(visibleBoids) for x in perceivedCenter)  # divides all tuple elements by the length
    if perceivedCenter != (
    0, 0):  # We need to check for "change" to avoid tendency towards the top left. (negative our position)
        perceivedCenter = vm.subVector2(perceivedCenter, centerBoidPosition)

    perceivedCenter = (x / coherenceFactor for x in
                       perceivedCenter)  # divides all tuple elements by the coherence factor
    return perceivedCenter


def separation(centerBoidPosition, tooCloseObjects):
    vec2 = (0, 0)
    for obj in tooCloseObjects:
        vec2 = vm.subVector2(vec2, vm.subVector2(obj.position, centerBoidPosition))
    return vec2


def alignment(centerBoidVelocity,visibleBoids,alignmentFactor):
    # Calculate the average velocity of all "visible" boids except this one and scale it by the alignment factor. Then return it
    averageVelocity = (0, 0)
    for boid in visibleBoids:
        averageVelocity = vm.addVector2(averageVelocity, boid.velocity)
    if len(visibleBoids) > 1:
        averageVelocity = (x / len(visibleBoids) for x in averageVelocity)  # divides all tuple elements by the length
    if averageVelocity != (
    0, 0):  # We need to check for "change" to avoid tendency towards the top left. (negative our position)
        averageVelocity = vm.subVector2(averageVelocity, centerBoidVelocity)

    averageVelocity = (x / alignmentFactor for x in
                       averageVelocity)  # divides all tuple elements by the alignment factor
    return averageVelocity


def findBoidsInRange(centerBoid, allObjects, range):
    return [obj for obj in allObjects if
            vm.calcVec2Distance(obj.position, centerBoid.position) <= range
            and obj != centerBoid]


def bounds(position, bounds, turnFactor):
    v = [0,0]
    if position[0] < bounds[0]:
        v[0] = turnFactor
    elif position[0] > bounds[0]+bounds[2]:
        v[0] = -turnFactor

    if position[1] < bounds[1]:
        v[1] = turnFactor
    elif position[1] > bounds[0]+bounds[3]:
        v[1] = -turnFactor

    return v