import pygame
from pygame.locals import *

class KeyboardInput():
    """Class for handling player input from the keyboard"""
    def __init__(self, keyList):
        self.keyList = keyList   

    def getPlayerInput(self, eventList):
        playerInput = ""
        for event in eventList:
            if event.type == KEYDOWN:
                if event.key == self.keyList['right']:
                    playerInput = 'right'
                if event.key == self.keyList['left']:
                    playerInput = 'left'
                if event.key == self.keyList['up']:
                    playerInput = 'up'
                if event.key == self.keyList['down']:
                    playerInput = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        return playerInput