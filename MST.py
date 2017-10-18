"""Implementation of the minimum spanning tree algorithm"""


# Relevant question
# Our graph is completely unweighted
# so we don't necessarily need the weighted parts of prim's and kruskal's algorithms.
# According to
# https://cs.stackexchange.com/questions/23179/if-all-edges-are-of-equal-weight-can-one-use-bfs-to-obtain-a-minimal-spanning-t
# /any/ spanning tree is a minimal spanning tree, so it works.
# The problem becomes to find a path from S to E
#
# Given a graph, G, with (S)tart and (E)nd
# Find a spanning-tree path from S to E, call this path P
# new Graph is now G - ¬P, ~= remove all edges that don't interfere with P
