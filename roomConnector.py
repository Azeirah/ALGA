from dfs import dfs
from graphUtils import countGridEdges

CUTPERCENTAGE = .1

def roomConnector():
    """Connects rooms in the underlying adjacency matrix (graph)
       constraints:
       1. Each room may only be connected to direct XY-coordinate neighbors
       2. Each room must be reachable

       Last update to this description: 17-10-2017 14:47:39
       The current implementation of this algorithm fulfills
       constraints 1 and 2,

       constraint 3 is very likely to be met

       constraint 4 is unknown atm

       20% * ~200connections ~= 40 on average, should be slightly less
    """


    numEdges = countGridEdges()
    edgesToCut = numEdges * CUTPERCENTAGE
