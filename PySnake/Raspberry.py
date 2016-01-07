import random

class Raspberry():
    """The raspberry that the snake must eat."""

    def __init__(self, block):
        """Creates a new instance of Raspberry"""
        #self.position = [15,15]
        self.spawn()
        self.block = block
        self.spawned = 1

    def spawn(self):
        """Spawns a new position for the Raspberry"""
        x = random.randrange(1,32)
        y = random.randrange(1,24)
        self.position = [x, y]
        self.spawned = 1

    def draw(self):
       """Draws the raspberry"""
       self.block.draw(self.position)


