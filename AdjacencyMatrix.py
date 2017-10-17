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
        self.amountOfNodes = amountOfNodes
        # initializes an empty array of size `n`
        self.nodes = [None] * amountOfNodes

        # fairly unreadable way to generate a 2d array in python
        self.adjacency = list(
            [list([0 for y in range(amountOfNodes)])
                     for x in range(amountOfNodes)]
        )

    def getAmountofNodes(self):
        return self.amountOfNodes

    def getNodes(self):
        return self.nodes

    def __str__(self):
        # x-axis
        s = "\t" + "\t".join([str(node.getID()) for node in self.nodes]) + "\n"
        for i in range(self.amountOfNodes):
            # y-axis
            row = str(i)
            for j in range(self.amountOfNodes):
                row += "\t" + str(self.adjacency[j][i])
            s += row + "\n"
        return s

    def addNode(self, x, node):
        self.nodes[x] = node

    def connectNodes(self, x, y):
        self.adjacency[y][x] = 1
        self.adjacency[x][y] = 1

    def getAllConnectedCells(self):
        """Gives you a list of connected cell tuples.
           Each tuple contains the ID's of two connected cells."""
        adjacents = []

        for y in range(self.amountOfNodes):
            for x in range(self.amountOfNodes):
                if self.adjacency[y][x] == 1:
                    adjacents.append((x, y))

        return adjacents
