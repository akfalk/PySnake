import pygame
from Block import PygameBlock
import sys, time
from Raspberry import Raspberry
from Snake import Snake

class GameArena():
    def __init__(self, size):
        self.size = size

    def updateScreen(self, raspberry, snakeList):
        raise Exception("GameArena.updateScreen is not to be called directly. Must be implemented by derived classes.")

    def createRaspberry(self):
        raise Exception("GameArena.createRaspberryBlock is not to be called directly. Must be implemented by derived classes.")

    def createSnakes(self):
       raise Exception("GameArena.createSnakeBlocks is not to be called directly. Must be implemented by derived classes.")

    def gameOver(self):
       raise Exception("GameArena.gameOver is not to be called directly. Must be implemented by derived classes.")

class PyGameArena(GameArena):
    redColour = pygame.Color(255, 0, 0)
    blackColour = pygame.Color(0, 0, 0)
    whiteColour = pygame.Color(255, 255, 255)
    greyColour = pygame.Color(150, 150, 150)

    def __init__(self,size, blockSize):
        GameArena.__init__(self, size)
        self.blockSize = blockSize
        self.playSurface = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Raspberry Snake')

    def createRaspberry(self):
        # define a PygameBlock. This block will contain all information about size, colour, and how to draw.
        raspberryBlock = PygameBlock(self.blockSize, self.redColour, self.playSurface)
        # The raspberryBlock is injected into the Raspberry object
        raspberry = Raspberry(raspberryBlock)
        return raspberry

    def createSnakes(self, playerInput):
        # define PygameBlocks for the two snakes
        snakeBlock_1 = PygameBlock(self.blockSize, self.whiteColour, self.playSurface)
        snakeBlock_2 = PygameBlock(self.blockSize, self.greyColour, self.playSurface)

        # create the snakes. The snakeBlocks are injected into the snakes
        snake_1 = Snake(snakeBlock_1, playerInput[0])
        snake_2 = Snake(snakeBlock_2, playerInput[1])
        return [snake_1, snake_2]

    def updateScreen(self, raspberry, snakeList):
        #put everything in position for redrawing...
        #...first the backdrop
        self.playSurface.fill(self.blackColour)

        # ...then draw snake
        for snake in snakeList:
            snake.draw(self.playSurface)

        # ...then draw raspberry
        raspberry.draw()

        # ...finally activte the update of the screen
        pygame.display.flip()

    def gameOver(self):
        gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
        gameOverSurf = gameOverFont.render('Game Over', True, self.greyColour)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (320, 10)
        self.playSurface.blit(gameOverSurf, gameOverRect)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()
