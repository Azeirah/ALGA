from AdjacencyMatrix import AdjacencyMatrix, Node
import random
import mapDrawing


def percentageChance(percentage):
    return random.random() < (percentage / 100)


dungeonConfig = {
    # amount of rooms = X * Y
    "X": 5,
    "Y": 5,
    "roomWidth": 7,
    "roomHeight": 7,
    "corridorLength": 3,
    "padding": 5
}


cellLookup = {
    "wall": "*",
    "empty": " ",
    "path": ".",
    "player": "♚",
    "start": "S",
    "end": "E"
}


class UndirectedUnweightedGraph(AdjacencyMatrix):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Map(UndirectedUnweightedGraph):
    """The map creates a 2d XY map out of an undirected acyclic graph"""

    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config = config

        # there is sequentiality inherent to these methods
        # they need to be executed in this order,
        # otherwise they don't make a lot of sense
        # that's why they're private
        self._initializeEmptyRooms()
        self._computeDungeonWidth()
        self._computeDungeonHeight()
        self._initializeEmptyCells()
        self._connectRooms()

    def _initializeEmptyRooms(self):
        """Fills the graph with empty, locationless, sizeless rooms"""
        for i in range(self.getAmountofNodes()):
            for j in range(self.getAmountofNodes()):
                self.addRoom(i)

    def _getNeighbors(self, roomIdx):
        nodes = self.getNodes()

        neighbors = []

        # left neighbor
        leftIdx = roomIdx - 1
        if 0 < leftIdx < self.amountOfNodes:
            neighbors.append(nodes[leftIdx])
        # right neighbor
        rightIdx = roomIdx + 1
        if 0 < rightIdx < self.amountOfNodes:
            neighbors.append(nodes[rightIdx])
        # upper neighbor
        upperIdx = roomIdx + self.config["X"]
        if 0 < upperIdx < self.amountOfNodes:
            neighbors.append(nodes[upperIdx])
        # lower neighbor
        lowerIdx = roomIdx - self.config["X"]
        if 0 < lowerIdx < self.amountOfNodes:
            neighbors.append(nodes[lowerIdx])

        return neighbors

    def _connectRooms(self):
        """Connects rooms in the underlying adjacency matrix (graph)
           constraints:
           1. Each room may only be connected to direct XY-coordinate neighbors
           2. Each room needs at least one connection
           3. Need an unknown amount more than 15 pathways at minimum
              requirements state that the grenade item
              should collapse 15 hallways (out of 5x5)
              but there should still be a path
              from current location to end location
           4. Cycles are required because the grenade
              item will collapse hallways
              but there should still be a path
              from your current room to the stairway

           Last update to this description: 17-10-2017 14:47:39
           The current implementation of this algorithm fulfills
           constraints 1 and 2,

           constraint 3 is very likely to be met

           constraint 4 is unknown atm

           20% * ~200connections ~= 40 on average, should be slightly less
        """

        # affects constraint#3 and constraint#4 statistically
        CONNECTIONCHANCE = 20

        for idx, room in enumerate(self.getNodes()):
            neighbors = self._getNeighbors(idx)
            print("All neighbors of {idx}:".format(idx=idx))
            for ID in map(lambda n: n.ID, neighbors):
                print(ID)

            # constraint#2, min one connection
            guaranteedConnection = random.choice(neighbors)
            self.connectNodes(idx, guaranteedConnection.ID)

            for neighbor in neighbors:
                if percentageChance(CONNECTIONCHANCE):
                    self.connectNodes(idx, neighbor.ID)

    def addRoom(self, x):
        self.addNode(x, Room(ID=x, config=self.config))

    def underlyingMatrixToStr(self):
        return super().__str__()

    def _initializeEmptyCells(self):
        self.theMap = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row += cellLookup["empty"]
            self.theMap.append(row)

    def getCell(self, x, y):
        """0-indexed"""
        return self.theMap[y][x]

    def setCell(self, x, y, content):
        self.theMap[y][x] = content

    def placeRooms(self, X, Y):
        currentRoomIdx = 0
        for x in range(X):
            for y in range(Y):
                uninitializedRoom = self.nodes[currentRoomIdx]
                uninitializedRoom.placeSelf(x, y, self)

                currentRoomIdx += 1

    def placeConnections(self):
        nodes = self.getNodes()
        for id1, id2 in self.getAllConnectedCells():
            neighbor = nodes[id2]
            nodes[id1].connectSelfToRoom(neighbor, self)

    def _computeDungeonWidth(self):
        # how many cells `X` rooms will maximally occupy
        maxRoomsWidth = self.config["X"] * self.config["roomWidth"]
        paddingWidth = 2 * self.config["padding"]
        corridorsWidth = \
            (self.config["X"] - 1) * self.config["corridorLength"]

        self.width = maxRoomsWidth + paddingWidth + corridorsWidth

    def _computeDungeonHeight(self):
        # how many cells `Y` rooms will maximally occupy
        maxRoomsHeight  = self.config["Y"] * self.config["roomHeight"]
        paddingHeight   = 2 * self.config["padding"]
        corridorsHeight = \
            (self.config["Y"] - 1) * self.config["corridorLength"]

        self.height = maxRoomsHeight + paddingHeight + corridorsHeight

    def __str__(self):
        m = "I am the map!\n"
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += self.getCell(x, y) + " "
            m += row + "\n"

        return m


class Dungeon():
    def __init__(self, dungeonConfig):
        self.config = dungeonConfig

        self.map = Map(
            amountOfNodes=self.config["X"] * self.config["Y"],
            config=dungeonConfig
        )

        self.map.placeRooms(self.config["X"], self.config["Y"])
        self.map.placeConnections()

    def __str__(self):
        s = "I am a dungeon of {x}x{y}\n".format(
            x=self.config["X"],
            y=self.config["Y"]
        )

        adjMatrStr = str(self.map)
        s += adjMatrStr

        return s


# the Room is a node
class Room(Node):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = config["roomWidth"]
        self.height = config["roomHeight"]
        self.config = config

    def placeSelf(self, x, y, dungeonMap):
        """Operates in map-domain, exists in graph-domain
           x and y arguments are in graph coordinates"""

        self.roomX = x
        self.roomY = y

        self.mapX = x * self.width + \
            x * self.config["corridorLength"] + \
            self.config["padding"]
        self.mapY = y * self.height + \
            y * self.config["corridorLength"] + \
            self.config["padding"]

        for w in range(self.width):
            for h in range(self.height):
                x = self.mapX + w
                y = self.mapY + h

                cell = cellLookup["path"]

                if w == 0 or w == self.width - 1:
                    cell = cellLookup["wall"]
                if h == 0 or h == self.height - 1:
                    cell = cellLookup["wall"]

                dungeonMap.setCell(x, y, cell)

    def getConnectorCoordinates(self, direction):
        """
               b
           ****a****
           *       *
        r  l       r  l
           *       *
           ****b****
               a

        gives back the relative-to-map coordinate
        for the requested location,
        (a)bove, (r)ight, (b)elow or (l)eft

        look at the letters in the room to choose what you want
        the letters on the outside are only to make it easy
        to determine relative directions
        """

        # self.mapX and self.mapY indicate top-left of the room
        halfWidth = self.width // 2
        halfHeight = self.height // 2

        endWidth = self.width - 1
        endHeight = self.height - 1

        if direction == "a":
            return (
                self.mapX + halfWidth,
                self.mapY
            )
        if direction == "r":
            return (
                self.mapX + endWidth,
                self.mapY + halfHeight
            )
        if direction == "b":
            return (
                self.mapX + halfWidth,
                self.mapY + endHeight
            )
        if direction == "l":
            return (
                self.mapX,
                self.mapY + halfHeight
            )

    def connectSelfToRoom(self, neighbor, dungeonMap):
        """Operates in map-domain, exists in graph-domain"""

        # case 1, neighbor is above self
        if self.roomY > neighbor.roomY and \
           self.roomX == neighbor.roomX:
            ownConnectorCoords = self.getConnectorCoordinates("a")
            neighborConnectorCoords = neighbor.getConnectorCoordinates("b")
            mapDrawing.drawVerticalLine(
                neighborConnectorCoords[1], ownConnectorCoords[1],
                ownConnectorCoords[0],
                "a",
                dungeonMap
            )

        # case 2, neighbor is left of self
        if self.roomY == neighbor.roomY and \
           self.roomX > neighbor.roomX:
            ownConnectorCoords = self.getConnectorCoordinates("l")
            neighborConnectorCoords = neighbor.getConnectorCoordinates("r")
            dx = abs(ownConnectorCoords[0] - neighborConnectorCoords[0])
            if dx > 5:
                print("drawing from")
                print(ownConnectorCoords)
                print("to")
                print(neighborConnectorCoords)
                print("dx = {dx}".format(dx=dx))
                print("IDS are id1={id1}, id2={id2}".format(id1=self.ID, id2=neighbor.ID))
                print()
            mapDrawing.drawHorizontalLine(
                neighborConnectorCoords[0], ownConnectorCoords[0],
                ownConnectorCoords[1],
                "l",
                dungeonMap
            )

        # case 3, neighbor is right of self
        if self.roomY == neighbor.roomY and \
           self.roomX < neighbor.roomX:
           pass

        # case 4, neighbor is below self
        if self.roomY < neighbor.roomY and \
           self.roomX == neighbor.roomX:
           pass


dungeon = Dungeon(dungeonConfig)
print(dungeon)
print(dungeon.map.underlyingMatrixToStr())
