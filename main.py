from AdjacencyMatrix import AdjacencyMatrix, Node
import random


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
        try:
            if nodes[roomIdx - 1] is not None:
                neighbors.append(nodes[roomIdx - 1])
        except Exception as e:
            pass
        # right neighbor
        try:
            if nodes[roomIdx + 1] is not None:
                neighbors.append(nodes[roomIdx + 1])
        except Exception as e:
            pass
        # upper neighbor
        try:
            if nodes[roomIdx + self.config["X"]] is not None:
                neighbors.append(nodes[roomIdx + self.config["X"]])
        except Exception as e:
            pass
        # lower neighbor
        try:
            if nodes[roomIdx - self.config["X"]] is not None:
                neighbors.append(nodes[roomIdx - self.config["X"]])
        except Exception as e:
            pass

        return neighbors

    def _connectRooms(self):
        """Connects rooms in the underlying adjacency matrix (graph)
           constraints:
           1. Each room may only be connected to direct XY-coordinate neighbors
           2. Each room needs at least one connection
           3. Need an unknown amount more than 15 pathways at minimum
              requirements state that the grenade item should collapse 15 hallways (out of 5x5)
              but there should still be a path from current location to end location
           4. Cycles are required because the grenade item will collapse hallways
              but there should still be a path from your current room to the stairway
        """

        # simple algorithm idea
        # 1. for room in rooms
        #     2. for neighbor in direct_neighbors(room)
        #         if chance(20%)
        #             connectRooms(room, neighbor)

        CONNECTIONCHANCE = 20

        for idx, room in enumerate(self.getNodes()):
            for neighbor in self._getNeighbors(idx):
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
                uninitializedRoom.place(x, y, self)

                currentRoomIdx += 1

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

    def place(self, x, y, dungeonMap):
        """x and y arguments are in graph coordinates"""

        self.x = x * self.width + \
            x * self.config["corridorLength"] + \
            self.config["padding"]
        self.y = y * self.height + \
            y * self.config["corridorLength"] + \
            self.config["padding"]

        for w in range(self.width):
            for h in range(self.height):
                x = self.x + w
                y = self.y + h

                cell = cellLookup["path"]

                if w == 0 or w == self.width - 1:
                    cell = cellLookup["wall"]
                if h == 0 or h == self.height - 1:
                    cell = cellLookup["wall"]

                dungeonMap.setCell(x, y, cell)


dungeon = Dungeon(dungeonConfig)
print(dungeon)
print(dungeon.map.underlyingMatrixToStr())
