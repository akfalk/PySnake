#!/usr/bin/env python

# Raspberry Snake
# Written by Gareth Halfacree for the Raspberry Pi User Guide
# grossly modified by akf towards an object-oriented design

from Raspberry import Raspberry
from Snake import Snake
import pygame, sys, time, random
from pygame.locals import *
from Block import PygameBlock
from GameArena import PyGameArena

pygame.init()

blockSize = 20

# frames per second - to be used as argument for pygame.time.Clock().tick in the forever loop
fps = 3

#create the game arena. The size of the arean is 32 by 24 units, each unit if of size "blockSize"
arena = PyGameArena([32,24], blockSize)

#create the raspberry
raspberry = arena.createRaspberry()

# define input keys for the two snakes
playerInput_1 = {'right':K_RIGHT, 'left':K_LEFT, 'up':K_UP, 'down':K_DOWN}
playerInput_2 = {'right':ord('d'), 'left':ord('a'), 'up':ord('w'), 'down':ord('s')}
playerInput = [playerInput_1, playerInput_2]
# create the snakes
snakeList = arena.createSnakes(playerInput)

def listenQuit(eventList):
    for event in eventList:
        if event.type == QUIT:
            pygame.quit()

while True:
    eventList = pygame.event.get()
    listenQuit(eventList)
    
    for snake in snakeList: 
        snake.getDirection(eventList)
        snake.move()

        if snake.checkPosition():
            arena.gameOver()

        snake.checkIntersect(snakeList)

        if snake.position == raspberry.position:
            # snake eats raspberry, spawn a new.
            raspberry.spawn()
            fps += 0.2
        else:
            # remove the tail - a new head has already been added - the snake will only grow longer when it takes a raspberry
            snake.segments.pop() #"pop" without an argument removes the last item of the list

    arena.updateScreen(raspberry, snakeList)

    # advance
    pygame.time.Clock().tick(fps)  # delay to "fps" frames per second

