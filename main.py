from Boid import Boid
import random
import sys, pygame

# Reference: http://www.kfish.org/boids/pseudocode.html

def BoidSimulation(count):
    size = width, height = 800, 600
    boids = [Boid((random.randint(0, width), random.randint(0, height))) for x in range(count)]
    pygame.init()
    black = 0, 0, 0
    labelfont = pygame.font.SysFont("Arial", 14)
    DSTR =  ("ID","VIEW","VELOCITY","PROTECTED")
    DEBUG = [DSTR[0],DSTR[3]] #TODO: Find better solution for this.

    screen = pygame.display.set_mode(size)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #Rule Toggle
                if event.key == pygame.K_1:
                    Boid.useCohesion = not Boid.useCohesion # or Boid.useCohesion ^= 1 <- XOR assignment operator
                if event.key == pygame.K_2:
                    Boid.useSeparation = not Boid.useSeparation
                if event.key == pygame.K_3:
                    Boid.useAlignment = not Boid.useAlignment

                #Debug Toggles
                if event.key == pygame.K_F1:
                    if DSTR[0] in DEBUG:
                        DEBUG.remove(DSTR[0])
                    else:
                        DEBUG.append(DSTR[0])

                if event.key == pygame.K_F2:
                    if DSTR[1] in DEBUG:
                        DEBUG.remove(DSTR[1])
                    else:
                        DEBUG.append(DSTR[1])

                if event.key == pygame.K_F3:
                    if DSTR[2] in DEBUG:
                        DEBUG.remove(DSTR[2])
                    else:
                        DEBUG.append(DSTR[2])

                if event.key == pygame.K_F4:
                    if DSTR[3] in DEBUG:
                        DEBUG.remove(DSTR[3])
                    else:
                        DEBUG.append(DSTR[3])

        screen.fill(black)
        for boid in boids:
            boid.draw(screen, debug=DEBUG)
            boid.move(boids)

        #Rule Labels
        label = labelfont.render("[1]:Cohesion            "+str(Boid.useCohesion), True, (255, 255, 255))
        screen.blit(label, (5, 5))
        label = labelfont.render("[2]:Separation          "+str(Boid.useSeparation), True, (255, 255, 255))
        screen.blit(label, (5, 25))
        label = labelfont.render("[3]:Alignment           "+str(Boid.useAlignment), True, (255, 255, 255))
        screen.blit(label, (5, 45))

        #Debug Labels ID/VIEW/VELOCITY/PROTECTED
        label = labelfont.render("[F1]:ID                      "+str("ID" in DEBUG), True, (255, 255, 255))
        screen.blit(label, (5, 65))
        label = labelfont.render("[F2]:VIEW                "+str("VIEW" in DEBUG), True, (255, 255, 255))
        screen.blit(label, (5, 85))
        label = labelfont.render("[F3]:VELOCITY       "+str("VELOCITY" in DEBUG), True, (255, 255, 255))
        screen.blit(label, (5, 105))
        label = labelfont.render("[F4]:PROTECTED  "+str("PROTECTED" in DEBUG), True, (255, 255, 255))
        screen.blit(label, (5, 125))

        #time.sleep(1)

        pygame.display.flip()


if __name__ == '__main__':
    BoidSimulation(200)
