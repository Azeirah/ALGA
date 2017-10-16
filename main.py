from AdjacencyMatrix import AdjacencyMatrix, Node


dungeonConfig = {
    # amount of rooms = X * Y
    "X": 5,
    "Y": 5,
    "minimumCorridorLength": 4,
    "maximumCorridorLength": None,  # not sure if this is necessary
    "maximumRoomWidth": 6,
    "maximumRoomHeight": 12,
    "padding": 5,
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

    def addRoom(self, x):
        self.addNode(x, Room(x))

    def underlyingMatrixToStr(self):
        return super().__str__()

    def generateRooms(self, X, Y):
        assert X * Y == self.getAmountofNodes()

        currentRoomIdx = 0
        for x in range(X):
            for y in range(Y):
                uninitializedRoom = self.nodes[currentRoomIdx]
                uninitializedRoom

                currentRoomIdx += 1

    def computeDungeonWidth(self):
        # how many cells `X` rooms will maximally occupy
        maxRoomsWidth = self.config["X"] * self.config["maximumRoomWidth"]
        paddingWidth = 2 * self.config["padding"]
        corridorsWidth = \
            (self.config["X"] - 1) * self.config["minimumCorridorLength"]

        self.width = maxRoomsWidth + paddingWidth + corridorsWidth

    def computeDungeonHeight(self):
        # how many cells `X` rooms will maximally occupy
        maxRoomsHeight  = self.config["Y"] * self.config["maximumRoomHeight"]
        paddingHeight   = 2 * self.config["padding"]
        corridorsHeight = \
            (self.config["Y"] - 1) * self.config["minimumCorridorLength"]

        self.height = maxRoomsHeight + paddingHeight + corridorsHeight

    def __str__(self):
        m = "I am the map!\n"
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                row += ". "
            m += row + "\n"

        return m


class Dungeon():
    def __init__(self, dungeonConfig):
        self.config = dungeonConfig

        self.map = Map(amountOfNodes=self.config["X"] * self.config["Y"], config=dungeonConfig)

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 5
        self.height = 5

    def __str__(self):
        return "room"


dungeon = Dungeon(dungeonConfig)
print(dungeon)
print(dungeon.map.underlyingMatrixToStr())
