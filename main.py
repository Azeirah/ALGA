import random

dungeonConfig = {
    "X": 5,
    "Y": 5
}


# adjency matrix info
# http://www.algolist.net/Data_structures/Graph/Internal_representation
class AdjacencyMatrix():
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

        self.storage = list(
            [list([y for y in range(Y)])
                     for x in range(X)]
        )

    def __str__(self):
        # x-axis
        s = "  " + "".join([str(s) for s in range(1, self.X + 1)]) + "\n"
        for i in range(self.X):
            # y-axis
            row = str(i + 1) + " "
            for j in range(self.Y):
                row += str(self.storage[j][i])
            s += row + "\n"
        return s

    def addRoom(self, j, i):
        self.storage[j][i] = Room()



# the Dungeon is a graph
class Dungeon():
    def __init__(self, dungeonConfig):
        self.X = dungeonConfig["X"]
        self.Y = dungeonConfig["Y"]

        # this line wins a beauty award
        self.adjacencyMatrix = AdjacencyMatrix(self.X, self.Y)
        # list(
        #     [list([y for y in range(self.Y)])
        #              for x in range(self.X)]
        # )

        self.generateRooms()

    def generateRooms(self):
        for i in range(self.X):
            for j in range(self.Y):
                self.adjacencyMatrix.addRoom(j, i)
                # self.adjacencyMatrix[j][i] = Room()

    def __str__(self):
        s = "I am a dungeon of {x}x{y}\n".format(x=self.X, y=self.Y)

        adjMatrStr = str(self.adjacencyMatrix)
        s += adjMatrStr

        return s


# the Room is a node
class Room():
    def __init__(self):
        self.exists = random.uniform(0, 100) < 30

    def __str__(self):
        if self.exists:
            return "1"
        else:
            return "0"


dungeon = Dungeon(dungeonConfig)
print(dungeon)
