"""Talisman command"""

from bfs import shortestPath

def talisman(dungeon):
    start, end = getStartEnd(dungeon.map)
    shortest = shortestPath(dungeon.map, start, end)

    try:
        distance = len(shortest) - 1
    except TypeError:
        distance = 0

    if distance == 0:
        return "You are in the staircase room!"
    else:
        return "The length of the shortest path is {lngth}".format(lngth=distance)



def getStartEnd(theMap):
    """Gets player position and staircase position"""
    return [theMap.nodes[ID] for ID in
                (theMap.player.position, theMap.staircase.position)]


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
    print(dungeon)

    talisman(dungeon)

    dungeon.map.player.move(dungeon.map.staircase.position)

    print("Moving player to staircase room {ID} and calling talisman".format(ID=dungeon.map.staircase.position))
    talisman(dungeon)
    dungeon.map.redraw()
    print(dungeon)
