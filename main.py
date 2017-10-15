import random
from AdjacencyMatrix import AdjacencyMatrix, Node


dungeonConfig = {
    # amount of rooms = X * Y
    "X": 5,
    "Y": 5
}


class UndirectedAcyclicGraph(AdjacencyMatrix):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Map(UndirectedAcyclicGraph):
    """The map creates a cartesian map out of an undirected acyclic graph"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def addRoom(self, x):
        self.addNode(x, Room(x))

    def underlyingMatrixToStr(self):
        return super().__str__()

    def __str__(self):
        return "The map ~~TODO~~\n\n\n"


class Dungeon():
    def __init__(self, dungeonConfig):
        self.X = dungeonConfig["X"]
        self.Y = dungeonConfig["Y"]
        self.size = self.X * self.Y

        self.map = Map(self.size)

        self.generateRooms()

    def generateRooms(self):
        for i in range(self.size):
            for j in range(self.size):
                self.map.addRoom(i)

    def __str__(self):
        s = "I am a dungeon of {x}x{y}\n".format(x=self.X, y=self.Y)

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
