import random


dungeonConfig = {
    # amount of rooms = X * Y
    "X": 5,
    "Y": 5
}


class Node():
    def __init__(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def __str__(self):
        return str(self.ID)


# adjency matrix info
# http://www.algolist.net/Data_structures/Graph/Internal_representation
class AdjacencyMatrix():
    def __init__(self, amountOfNodes):
        self.n = amountOfNodes
        # initializes an empty array of size `n`
        self.nodes = [None] * amountOfNodes

        # fairly unreadable way to generate a 2d array in python
        self.adjacency = list(
            [list([0 for y in range(amountOfNodes)])
                     for x in range(amountOfNodes)]
        )

    def __str__(self):
        # x-axis
        s = "\t" + "\t".join([str(node.getID()) for node in self.nodes]) + "\n"
        for i in range(self.n):
            # y-axis
            row = str(i + 1)
            for j in range(self.n):
                row += "\t" + str(self.adjacency[j][i])
            s += row + "\n"
        return s

    def addNode(self, x, node):
        self.nodes[x] = node

    def connectNodes(self, x, y):
        self.adjacency[y][x] = 1
        self.adjacency[x][y] = 1


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
