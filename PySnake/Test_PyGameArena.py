import pygame, time
from pygame.locals import *
from Block import PygameBlock
from GameArena import PyGameArena
from Raspberry import Raspberry
from Snake import Snake

#test PyGameArena
pygame.init()

blockSize = 20

#create the game arena
arena = PyGameArena([32,24], 20)

#create the raspberry
raspberry = arena.createRaspberry()

# define input keys for the two snakes
playerInput_1 = {'right':K_RIGHT, 'left':K_LEFT, 'up':K_UP, 'down':K_DOWN}
playerInput_2 = {'right':ord('d'), 'left':ord('a'), 'up':ord('w'), 'down':ord('s')}
playerInput = [playerInput_1, playerInput_2]
# create the snakes
snakeList = arena.createSnakes(playerInput)

arena.updateScreen(raspberry, snakeList)

time.sleep(5)

arena.gameOver()