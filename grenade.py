"""Grenade command"""
from mst import mst
from graphUtils import isMST


class Grenade():
    def __init__(self, theMap):
        self.map = theMap

        self.removedEdges = ()

    def draw(self):
        nodes = self.map.getAllNodes()
        for id1, id2, in self.removedEdges:
            neighbor = nodes[id2]
            nodes[id1].drawRoomConnection(neighbor,
                                          self.map,
                                          cellType="destroyedWall")

    def hasExploded(self):
        return len(self.removedEdges) > 0

    def explode(self):
        graph = self.map

        edges = graph.getAllEdges()
        keepTheseEdges = mst(self.map)
        removeTheseEdges = edges - keepTheseEdges

        for e1, e2 in removeTheseEdges:
            graph.disconnectNodes(e1, e2)

        self.removedEdges = removeTheseEdges


if __name__ == "__main__":
    from main import Dungeon

    dungeonConfig = {
        # amount of rooms = X * Y
        "X": 4,
        "Y": 4,
        "roomWidth": 5,
        "roomHeight": 5,
        "corridorLength": 3,
        "padding": 5,
        "showID": True
    }

    dungeon = Dungeon(dungeonConfig)
    print("*"*80)
    print("*"*80)
    print("BEFORE GRENADE")
    print("*"*80)
    print("*"*80)
    print(dungeon)

    dungeon.map.grenade.explode()
    dungeon.map.redraw()

    print("*"*80)
    print("*"*80)
    print("AFTER GRENADE")
    print("*"*80)
    print("*"*80)
    print(dungeon)

    print("is the dungeon an mst now?", isMST(dungeon.map))

