import pygame
from pygame.locals import *

class Snake():
    "Contains the snake"

    def __init__(self, block, playerInput):
        self.position = [5,5]
        self.segments = [[5,5],[4,5],[3,5]]
        self.direction = 'right'
        self.block = block
        self.playerInput = playerInput
        self.life = 3

    def getDirection(self, eventList):
        changeDirection = self.playerInput.getPlayerInput(eventList)
        if changeDirection == 'right' and not self.direction == 'left':
            self.direction = changeDirection
        if changeDirection == 'left' and not self.direction == 'right':
            self.direction = changeDirection
        if changeDirection == 'up' and not self.direction == 'down':
            self.direction = changeDirection
        if changeDirection == 'down' and not self.direction == 'up':
            self.direction = changeDirection

    def move(self):
        if self.direction == 'right':
            self.position[0] += 1
        if self.direction == 'left':
            self.position[0] -= 1
        if self.direction == 'up':
            self.position[1] -= 1
        if self.direction == 'down':
            self.position[1] += 1
        self.segments.insert(0,list(self.position)) #The new snakehead

    def checkPosition(self):
        gameOver = False
        # check if outside of x-borders
        if self.position[0] > 31 or self.position[0] < 0:
            gameOver = True
  
        # check if outside of y-borders
        if self.position[1] > 23 or self.position[1] < 0:
            gameOver = True

        # check if snake crosses itself
        if self.position in self.segments[1:]:
            gameOver = True

        return gameOver

    def checkIntersect(self, snakeList):
        for snake in snakeList:
            if self != snake:
                if self.position in snake.segments[1:]:
                    self.life -= 1
                    print snake, "looses one life"
            
    def draw(self, playSurface):
        for position in self.segments:
            self.block.draw(position)