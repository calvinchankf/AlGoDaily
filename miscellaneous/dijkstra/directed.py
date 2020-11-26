import heapq

"""
    dijkstra on a directed graph:
    find the shortest path(least weight) from one node to all the nodes
    
    Time    O((E + V) x logV)
    Space   O(V)
"""


def dijkstra(edges, p, q):
    """
    :type edges: List[List[int]]
    :type p: string, id for the start point
    :type q: string, id for the end point
    :rtype: [string], the path with min cost
    """
    # get all nodes
    nodeSet = set()
    for edge in edges:
        nodeSet.add(edge[0])
        nodeSet.add(edge[1])
    nodes = list(nodeSet)
    # adjacent list
    connections = {}
    # edge with cost { from: (to, cost), ... }
    for src, dest, cost in edges:
        if src in connections:
            connections[src].append((dest, cost))
        else:
            connections[src] = [(dest, cost)]
    # dijkstra's
    # put (cost, node, visitedpath) into the heap
    heap = [(0, p, [])]
    best = {}
    while len(heap) > 0:
        # pop the edge with min cost
        cost, node, path = heapq.heappop(heap)
        # if the cost < calculated cost of the node, update the node
        if node in best and cost >= best[node][0]:
            continue
        newPath = path + [node]
        best[node] = (cost, newPath)
        # add the adjacent nodes to the pq for processing
        if node in connections:
            candidates = connections[node]
            for can in candidates:
                heapq.heappush(heap, (cost+can[1], can[0], newPath))

    return best[q][1]


# normal case: https://www.youtube.com/watch?v=_lHSawdgXpI
r = [
    ['A', 'B', 4],
    ['A', 'C', 2],
    ['B', 'C', 3],
    ['C', 'B', 1],
    ['B', 'D', 2],
    ['B', 'E', 3],
    ['C', 'D', 4],
    ['C', 'E', 5],
    ['D', 'E', 1],
]
# ['A', 'C', 'B', 'E']
print(dijkstra(r, 'A', 'E'))
