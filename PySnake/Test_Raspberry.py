import pygame, time
from Raspberry import Raspberry
from Block import PygameBlock

#test Raspberry
pygame.init()
playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Block test')

redColour = pygame.Color(255, 0, 0)
redBlock = PygameBlock(20, redColour, playSurface)
raspberry = Raspberry(redBlock)

#...first the backdrop
blackColour = pygame.Color(0, 0, 0)
playSurface.fill(blackColour)

raspberry.draw()

# ...finally activte the update of the screen
pygame.display.flip()

raspberry.spawn()
print "raspberry.position = ", raspberry.position

time.sleep(5)
pygame.quit()
