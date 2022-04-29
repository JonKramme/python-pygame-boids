from Boid import Boid
import random
import sys, pygame

# Reference: http://www.kfish.org/boids/pseudocode.html

def BoidSimulation(count):
    size = width, height = 800, 600
    boids = [Boid((random.randint(0, width), random.randint(0, height))) for x in range(count)]
    pygame.init()
    black = 0, 0, 0
    labelfont = pygame.font.SysFont("Arial", 20)

    screen = pygame.display.set_mode(size)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Boid.useCohesion = not Boid.useCohesion
                if event.key == pygame.K_2:
                    Boid.useSeparation = not Boid.useSeparation
                if event.key == pygame.K_3:
                    Boid.useAlignment = not Boid.useAlignment

        screen.fill(black)
        for boid in boids:
            boid.draw(screen, debug="id/velocity")
            boid.move(boids)

        label = labelfont.render("[1]:Cohesion   "+str(Boid.useCohesion), True, (255, 255, 255))
        screen.blit(label, (5, 5))
        label = labelfont.render("[2]:Separation "+str(Boid.useSeparation), True, (255, 255, 255))
        screen.blit(label, (5, 25))
        label = labelfont.render("[3]:Alignment  "+str(Boid.useAlignment), True, (255, 255, 255))
        screen.blit(label, (5, 45))

        #time.sleep(1)

        pygame.display.flip()


if __name__ == '__main__':
    BoidSimulation(200)
