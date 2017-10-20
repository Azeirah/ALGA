from cellLookup import cellLookup

class Player():
    def __init__(self, theMap):
        # position tracks a room index, that is, an AdjacentMatrix ID
        self.position = 0

        # keep track of the map, (map is a keyword, don't override it)
        self.map = theMap

    def draw(self):
        room = self.map.nodes[self.position]
        coords = room.getConnectorCoordinates("c")
        self.map.setCell(coords[0], coords[1], cellLookup["player"])

    def movePlayer(self, roomIdx):
        """Player position is the idx of a graph node."""
        self.position = roomIdx
