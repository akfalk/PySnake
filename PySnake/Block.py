import pygame
from pygame.locals import *

class Block():
    """ The smallest element in the program. Used to draw Snake, Raspberry and Border"""

    def __init__(self, size):
        self.size = size 

    def draw(self, position):
        raise Exception ('Block.draw is intended as a virtual method that must be overridden by all classes derived from Block. It should not be called directly.\n')
    
class PygameBlock(Block):
    def __init__(self, size, colour, playSurface):
        Block.__init__(self, size)
        self.colour = colour
        self.playSurface = playSurface

    def draw(self, position):
        x = int(position[0]*self.size)
        y = int(position[1]*self.size)
        pygame.draw.rect(self.playSurface,self.colour,Rect(x, y, self.size, self.size))
        #pygame.draw.rect(self.playSurface,self.colour,Rect(position[0], position[1], self.size, self.size))

"""test exception
block = Block(20, [300,300])
block.draw()
"""

"""
#test PygameBlock
pygame.init()
playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Block test')

testColour = pygame.Color(255, 0, 0)
testBlock = PygameBlock(20, [300,300], testColour, playSurface)

#...first the backdrop
blackColour = blackColour = pygame.Color(0, 0, 0)
playSurface.fill(blackColour)

testBlock.draw()

# ...finally activte the update of the screen
pygame.display.flip()

time.sleep(5)
pygame.quit()
"""

