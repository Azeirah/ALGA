import random

dungeonConfig = {
    # amount of rooms = X * Y
    "X": 5,
    "Y": 5
}


# adjency matrix info
# http://www.algolist.net/Data_structures/Graph/Internal_representation
class AdjacencyMatrix():
    def __init__(self, amountOfNodes):
        self.n = amountOfNodes

        self.storage = list(
            [list([0 for y in range(amountOfNodes)])
                     for x in range(amountOfNodes)]
        )

    def __str__(self):
        # x-axis
        s = "\t" + "\t".join([str(s) for s in range(1, self.n + 1)]) + "\n"
        for i in range(self.n):
            # y-axis
            row = str(i + 1)
            for j in range(self.n):
                row += "\t" + str(self.storage[j][i])
            s += row + "\n"
        return s

    def addNode(self, x, content):
        self.storage[x][x] = content

    def connectNodes(self, x1, y1, x2, y2):
        self.storage


class UndirectedAcyclicGraph(AdjacencyMatrix):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Map(UndirectedAcyclicGraph):
    """The map visualizes the undirected acyclic graph filled with rooms
       as a 2D roguelike dungeon"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def addRoom(self, x):
        newRoom = Room()
        self.addNode(x, newRoom)

    def underlyingMatrixToStr(self):
        return super().__str__()

    def __str__(self):
        return "The map ~~TODO~~\n\n\n"


class Dungeon():
    def __init__(self, dungeonConfig):
        self.X = dungeonConfig["X"]
        self.Y = dungeonConfig["Y"]
        self.size = self.X * self.Y

        self.map = Map(self.X * self.Y)

        self.generateRooms()

    def generateRooms(self):
        for i in range(self.size):
            for j in range(self.size):
                if random.uniform(0, 100) < 30:
                    self.map.addRoom(i)

    def __str__(self):
        s = "I am a dungeon of {x}x{y}\n".format(x=self.X, y=self.Y)

        adjMatrStr = str(self.map)
        s += adjMatrStr

        return s


# the Room is a node
class Room():
    def __init__(self):
        self.width = 5
        self.height = 5

    def __str__(self):
        return "1"


dungeon = Dungeon(dungeonConfig)
print(dungeon)
print(dungeon.map.underlyingMatrixToStr())
