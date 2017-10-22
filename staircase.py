from cellLookup import cellLookup
import random


class Staircase():
    """The staircase is the end of the dungeon"""

    def __init__(self, theMap):
        # position tracks the position of the staircase
        # as a AdjacencyMatrix ID
        self.map = theMap

        self.position = self.positionStaircase()

    def draw(self):
        room = self.map.nodes[self.position]
        coords = room.getConnectorCoordinates("c")
        self.map.setCell(coords[0], coords[1], cellLookup["staircase"])

    def positionStaircase(self):
        """The position of the staircase is determined by a randomish formula"""
        nodes = self.map.getAmountofNodes()

        # since the player always starts at the
        # top-left corner with ID=0
        #
        # we can pick a room that's far away from
        # the player by simply staying in the higher IDs range

        x, y = self.map.config["X"], self.map.config["Y"]

        minimum = (x - 1) * (y - 1)
        maximum = (  x    *    y  ) - 1

        return random.randint(minimum, maximum)
