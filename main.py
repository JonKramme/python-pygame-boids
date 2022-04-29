from Boid import Boid
import random
import sys, pygame

# Reference: http://www.kfish.org/boids/pseudocode.html

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
            boid.draw(screen,debug="id/velocity")
            boid.move(boids)
        #time.sleep(1)

        pygame.display.flip()


if __name__ == '__main__':
    BoidSimulation(200)
