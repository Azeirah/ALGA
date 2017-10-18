"""Utilities for unclassified or random graph-related stuff"""

def countGridEdges(x, y):
    """
      x
    ------>
    *-*-*-* |
    | | | | |
    *-*-*-* |
    | | | | | y
    *-*-*-* |
    | | | | |
    *-*-*-* v

    is a grid. Counts the number of edges given its dimensions
    """

    return 2 * x * y - x - y
