import random
import sys, pygame


# Reference: http://www.kfish.org/boids/pseudocode.html

class Boid():
    def __init__(self, pos):
        self.position = pos
        self.velocity = (random.randint(-1, 1), random.randint(-1, 1))
        self.protectedRange = 2
        self.viewRange = 20
        self.coherenceFactor = 100

    def draw(self, screen, debug="off"):
        # print(self.position)
        pygame.draw.circle(screen, (255, 255, 255), tuple(map(int, self.position)), 1)
        if debug == "view":
            pygame.draw.circle(screen, (255, 0, 0), tuple(map(int, self.position)), self.viewRange)
        if debug == "protected":
            pygame.draw.circle(screen, (255, 0, 0), tuple(map(int, self.position)), self.protectedRange)

    def move(self, allBoids):
        visibleBoids = self.findVisibleBoids(allBoids)
        tooCloseBoids = self.findTooCloseBoids(visibleBoids)
        v1 = self.coherence(visibleBoids)
        self.velocity = (self.velocity[0] + v1[0],
                         self.velocity[1] + v1[1])  # + self.separation(tooCloseBoids) + self.alignment(visibleBoids)
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def coherence(self, visibleBoids):
        # Calculate the center position of all "visible" boids except this one, calculate direction vector
        # towards that point and scale it by the coherence Factor. Then return it
        percievedCenter = [0, 0]
        for boid in visibleBoids:
            percievedCenter = self.addVector3(percievedCenter, boid.position)
        if len(visibleBoids) > 0:
            percievedCenter = [x / len(visibleBoids) for x in percievedCenter]
        percievedCenter = self.subVector3(percievedCenter, self.position)
        percievedCenter = [x / self.coherenceFactor for x in percievedCenter]
        return tuple(percievedCenter)

    def addVector3(self, v1, v2, *args):
        vecList = [v1, v2, *args]
        vec = (0, 0)
        for x in vecList:
            vec = tuple(map(lambda i, j: i + j, vec, x))
        return vec

    def subVector3(self, v1, v2, *args):
        vecList = [v1, v2, *args]
        vec = (0, 0)
        for x in vecList:
            vec = tuple(map(lambda i, j: i - j, vec, x))
        return vec

    def separation(self, tooCloseBoids):
        pass

    def alignment(self, visibleBoids):
        pass

    def findVisibleBoids(self, allBoids):
        boidlist = allBoids.copy()
        boidlist.remove(self)
        return [boid for boid in boidlist if
                (abs(boid.position[0] - self.position[0] + boid.position[1] - self.position[1])) <= self.viewRange]

    def findTooCloseBoids(self, allBoids):
        boidlist = allBoids.copy()  # No need to remove self as we only pass the visible boids to this function
        return [boid for boid in boidlist if (abs(boid.position[0] - self.position[0]) + abs(
            boid.position[1] - self.position[1])) <= self.protectedRange]


def BoidSimulation(count):
    size = width, height = 800, 600
    boids = [Boid((random.randint(0, width), random.randint(0, height))) for x in range(count)]
    pygame.init()
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)
        for boid in boids:
            boid.draw(screen)
            boid.move(boids)

        pygame.display.flip()


if __name__ == '__main__':
    BoidSimulation(200)
