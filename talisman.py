"""Talisman command"""

from bfs import shortestPath

def talisman(dungeon):
    pass



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

    talisman(dungeon)
    dungeon.map.redraw()

    print("is the dungeon an mst now?", isMST(dungeon.map))

