"""Grenade command"""
from mst import mst
from graphUtils import isMST

def grenade(dungeon):
    graph = dungeon.map
    edges = graph.getAllEdges()
    keepTheseEdges = mst(dungeon.map)
    removeTheseEdges = edges - keepTheseEdges

    for e1, e2 in removeTheseEdges:
        graph.disconnectNodes(e1, e2)


if __name__ == "__main__":
    from main import Dungeon

    dungeonConfig = {
        # amount of rooms = X * Y
        "X": 7,
        "Y": 7,
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

    grenade(dungeon)
    dungeon.map.redraw()

    print("*"*80)
    print("*"*80)
    print("AFTER GRENADE")
    print("*"*80)
    print("*"*80)
    print(dungeon)

    print("is the dungeon an mst now?", isMST(dungeon.map))

