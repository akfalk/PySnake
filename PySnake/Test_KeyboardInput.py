import pygame
from pygame.locals import *
from PlayerInput import KeyboardInput

pygame.init()

# It seems that pygame needs a display to detect key-pressed events...
# Tried os.environ["SDL_VIDEODRIVER"] = "dummy", but the the event queue staysempty even though the keys are pressed.
# Tried pygame.event.pump() in the forever loop, but no events were added to the queue without a display.
# SOLUTION: The pygame.NOFRAME does not draw the display, but lets it react to pressing keys
pygame.display.set_mode((1,1), pygame.NOFRAME)

playerInput_1 = {'right':K_RIGHT, 'left':K_LEFT, 'up':K_UP, 'down':K_DOWN}
input = KeyboardInput(playerInput_1)

def listenQuit(eventList):
    for event in eventList:
        if event.type == QUIT:
            pygame.quit()

while True:
    eventList = pygame.event.get()
    listenQuit(eventList)

    direction = 'right'

    print input.getPlayerInput(eventList)

    # advance
    pygame.time.Clock().tick(1)  # delay to 1 frames per second


