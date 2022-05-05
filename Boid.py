import itertools
import VectorMath as vm
import BoidBehaviour as bh
import random

import pygame


class Boid():
    id_iterator = itertools.count()
    useCohesion = True
    useSeparation = True
    useAlignment = True
    limitSpeed = True
    useBounds = True

    def __init__(self, pos,bounds):
        self.id = next(Boid.id_iterator)
        self.position = pos
        self.velocity = (-1 + random.random() * 2, -1 + random.random() * 2)
        self.protectedRange = 8
        self.viewRange = 40
        self.coherenceFactor = 80
        self.alignmentFactor = 8
        self.maxVelocity = (5, 5)
        self.turnFactor = 5
        self.bounds = bounds

    def draw(self, screen, debug=()):
        #Always draw the Boid:
        pygame.draw.circle(screen, (255, 255, 255), tuple(map(int, self.position)), 2)

        #Draw Debug Variants:
        if "VIEW" in debug:
            pygame.draw.circle(screen, (255, 0, 0), tuple(map(int, self.position)), self.viewRange, 1)
        if "PROTECTED" in debug:
            pygame.draw.circle(screen, (180, 0, 0), tuple(map(int, self.position)), self.protectedRange,1)
        if "VELOCITY" in debug:
            pygame.draw.line(screen, (255, 0, 0), tuple(map(int, self.position)),
                             vm.addVector2(tuple(map(int, self.position)), self.velocity))
        if "ID" in debug:
            labelfont = pygame.font.SysFont("Arial", 15)
            label = labelfont.render(str(self.id), True, (255, 255, 255))
            screen.blit(label, tuple(map(int, self.position)))
        if "BOUNDS" in debug:
            pygame.draw.rect(screen,(255,255,255), self.bounds, 1)

    def move(self, allBoids):
        visibleBoids = bh.findBoidsInRange(self, allBoids, self.viewRange)
        tooCloseBoids = bh.findBoidsInRange(self, allBoids, self.protectedRange)
        # currently only Boids exist. If Other Objects are added
        # we will have to pass them to the function above function.

        if Boid.useCohesion:
            self.velocity = vm.addVector2(self.velocity, bh.coherence(self.position,visibleBoids,self.coherenceFactor))
        if Boid.useSeparation:
            self.velocity = vm.addVector2(self.velocity, bh.separation(self.position,tooCloseBoids))
        if Boid.useAlignment:
            self.velocity = vm.addVector2(self.velocity, bh.alignment(self.velocity,visibleBoids,self.alignmentFactor))
        if Boid.useBounds:
            self.velocity = vm.addVector2(self.velocity, bh.bounds(self.position,self.bounds, self.turnFactor))

        if self.limitSpeed:
            vm.limit_velocity(self)
        self.position = vm.addVector2(self.position, self.velocity)
