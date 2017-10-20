class Node():
    def __init__(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def __str__(self):
        return str(self.ID)

    def deepCopy(self):
        return Node(self.ID)

    def __repr__(self):
        return "AdjacencyMatrix.Node ID={ID}".format(ID=self.ID)


# adjency matrix info
# http://www.algolist.net/Data_structures/Graph/Internal_representation
class AdjacencyMatrix():
    def __init__(self, amountOfNodes):
        self.amountOfNodes = amountOfNodes
        # initializes an empty array of size `n`
        self.nodes = [Node(i) for i in range(amountOfNodes)]

        # fairly unreadable way to generate a 2d array in python
        self.adjacency = list(
            [list([0 for y in range(amountOfNodes)])
                     for x in range(amountOfNodes)]
        )

    def getAmountofNodes(self):
        return self.amountOfNodes

    def getAllNodes(self):
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

    def disconnectNodes(self, x, y):
        self.adjacency[y][x] = 0

    def getAllEdges(self):
        """Gives you an iterable of connected node tuples.
           Each tuple contains the ID's of two connected cells."""
        adjacents = set()

        for y in range(self.amountOfNodes):
            for x in range(self.amountOfNodes):
                if self.adjacency[y][x] == 1:
                    adjacents.add((x, y))

        return adjacents

    def getAllNodesConnectedTo(self, node):
        """Gives you a list of nodes connected to the given node"""
        connections = set()

        try:
            node.getID()
        except:
            # node can be passed as its ID
            node = self.nodes[node]

        for y in range(self.amountOfNodes):
            if self.adjacency[y][node.getID()] == 1:
                connections.add(self.nodes[y])

        return connections

    def deepCopy(self):
        copy = AdjacencyMatrix(self.amountOfNodes)

        for node in self.nodes:
            copy.addNode(node.ID, node.deepCopy())

        for x, y in self.getAllEdges():
            copy.connectNodes(x, y)

        return copy


if __name__ == "__main__":
    g1 = AdjacencyMatrix(5)
    g1.connectNodes(1, 3)
    g1.connectNodes(2, 4)
    g1.connectNodes(2, 3)

    print("testcase for deepcopy")
    print("g1 should equal g1's deepcopy")
    print(str(g1.deepCopy()) == str(g1))
