import VectorMath as vm
def coherence(position,visibleBoids, coherenceFactor):
    # Calculate the center position of all "visible" boids except this one, calculate direction vector
    # towards that point and scale it by the coherence Factor. Then return it
    perceivedCenter = (0, 0)
    for boid in visibleBoids:
        perceivedCenter = vm.addVector2(perceivedCenter, boid.position)
    if len(visibleBoids) > 1:
        perceivedCenter = (x / len(visibleBoids) for x in perceivedCenter) #divides all tuple elements by the length
    perceivedCenter = vm.subVector2(perceivedCenter, position)
    perceivedCenter = (x / coherenceFactor for x in perceivedCenter) #divides all tuple elements by the coherence factor
    return perceivedCenter


def separation( tooCloseBoids):
    vec2 = (0, 0)


def separation( tooCloseObjects):
    pass


def alignment( visibleBoids):
    pass


def findBoidsInRange(centerBoid,allObjects,range):
    return [obj for obj in allObjects if
            vm.calcVec2Distance(obj.position, centerBoid.position) <= range
            and obj != centerBoid]


