import itertools
import random
import sys, pygame
import time

# Reference: http://www.kfish.org/boids/pseudocode.html


class Boid():
    id_iterator = itertools.count()
    def __init__(self, pos):
        self.id = next(Boid.id_iterator)
        self.position = pos
        self.velocity = (-1+random.random()*2, -1+random.random()*2)
        self.protectedRange = 2
        self.viewRange = 20
        self.coherenceFactor = 100
        self.maxSpeed = 2


    def draw(self, screen, debug="off"):
        # print(self.position)
        pygame.draw.circle(screen, (255, 255, 255), tuple(map(int, self.position)), 2)
        if "view" in debug:
            pygame.draw.circle(screen, (255, 0, 0), tuple(map(int, self.position)), self.viewRange)
        if "protected" in debug:
            pygame.draw.circle(screen, (255, 0, 0), tuple(map(int, self.position)), self.protectedRange)
        if "ID" in debug:
            pygame.draw.circle(screen, (255, 0, 0), tuple(map(int, self.position)), self.protectedRange)

    def move(self, allBoids):
        visibleBoids = self.findVisibleBoids(allBoids)
        tooCloseBoids = self.findTooCloseObjects(allBoids) # currently only Boids exist. If Other Objects are added
                                                               # we will have to pass them to this function.

        self.velocity = self.addVector2(self.velocity, self.coherence(visibleBoids)) # + self.separation(tooCloseBoids) + self.alignment(visibleBoids)
        self.position = self.addVector2(self.position, self.limitSpeed(self.velocity))
    def coherence(self, visibleBoids):
        # Calculate the center position of all "visible" boids except this one, calculate direction vector
        # towards that point and scale it by the coherence Factor. Then return it
        percievedCenter = (0, 0)
        for boid in visibleBoids:
            percievedCenter = self.addVector2(percievedCenter, boid.position)
        if len(visibleBoids) > 1:
            percievedCenter = [x / len(visibleBoids) for x in percievedCenter]
        percievedCenter = self.subVector2( percievedCenter,self.position)
        percievedCenter = [x / self.coherenceFactor for x in percievedCenter]
        return percievedCenter

    def separation(self,TooCloseBoids):
        vec2 = (0,0)



    def limitSpeed(self,vector2):
        vec = ()
        for x in vector2:
            if x >= self.maxSpeed:
                vec+=self.maxSpeed,
            elif x <= -self.maxSpeed:
                vec+=-self.maxSpeed,
            else:
                vec+=x,
        return vec

    def addVector2(self, v1, v2, *args):
        vecList = [v1, v2, *args]
        vec = (0, 0)
        for x in vecList:
            vec = tuple(map(lambda i, j: i + j, vec, x))

        return vec

    def subVector2(self, v1, v2, *args):
        vecList = [v1, v2, *args]
        vec = (0, 0)
        for x in vecList:
            vec = tuple(map(lambda i, j: i - j, vec, x))
        return vec

    def separation(self, tooCloseObjects):
        pass

    def alignment(self, visibleBoids):
        pass

    def findVisibleBoids(self, allBoids):
        return [boid for boid in allBoids if
                (abs(boid.position[0] - self.position[0] + boid.position[1] - self.position[1])) <= self.viewRange
                and boid != self]

    def findTooCloseObjects(self, allObjects):
        return [obj for obj in allObjects if
                (abs(obj.position[0] - self.position[0] + obj.position[1] - self.position[1])) <= self.protectedRange
                and obj != self]


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
            boid.draw(screen,debug="view")
            boid.move(boids)
        #time.sleep(1)

        pygame.display.flip()


if __name__ == '__main__':
    BoidSimulation(200)
