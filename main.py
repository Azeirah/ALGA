from AdjacencyMatrix import AdjacencyMatrix, Node
from pprint import pprint

dungeonConfig = {
    # amount of rooms = X * Y
    "X": 5,
    "Y": 5,
    "roomWidth": 5,
    "roomHeight": 5,
    "corridorLength": 3,
    "padding": 5
}


class UndirectedAcyclicGraph(AdjacencyMatrix):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Map(UndirectedAcyclicGraph):
    """The map creates a cartesian map out of an undirected acyclic graph"""

    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config = config

        # Fills the graph with empty, locationless, sizeless rooms
        for i in range(self.getAmountofNodes()):
            for j in range(self.getAmountofNodes()):
                self.addRoom(i)

        self.computeDungeonWidth()
        self.computeDungeonHeight()
        self.initializeEmptyCells()

    def addRoom(self, x):
        self.addNode(x, Room(ID=x, config=self.config))

    def underlyingMatrixToStr(self):
        return super().__str__()

    def initializeEmptyCells(self):
        self.theMap = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row += "."
            self.theMap.append(row)

    def getCell(self, x, y):
        """0-indexed"""
        return self.theMap[y][x]

    def setCell(self, x, y, content):
        self.theMap[y][x] = content

    def generateRooms(self, X, Y):
        currentRoomIdx = 0
        for x in range(X):
            for y in range(Y):
                uninitializedRoom = self.nodes[currentRoomIdx]
                uninitializedRoom.place(x, y, self)

                currentRoomIdx += 1

    def computeDungeonWidth(self):
        # how many cells `X` rooms will maximally occupy
        maxRoomsWidth = self.config["X"] * self.config["roomWidth"]
        paddingWidth = 2 * self.config["padding"]
        corridorsWidth = \
            (self.config["X"] - 1) * self.config["corridorLength"]

        self.width = maxRoomsWidth + paddingWidth + corridorsWidth

    def computeDungeonHeight(self):
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

        self.map.generateRooms(self.config["X"], self.config["Y"])

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
                dungeonMap.setCell(self.x + w, self.y + h, "X")

    def __str__(self):
        return "room"


dungeon = Dungeon(dungeonConfig)
print(dungeon)
print(dungeon.map.underlyingMatrixToStr())
