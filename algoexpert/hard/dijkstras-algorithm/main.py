from heapq import *

"""
    Time    O((E + V) x logV)
    Space   O(V)
"""


def dijkstrasAlgorithm(start, edges):
    n = len(edges)
    minheap = [(0, start)]
    caches = n * [2**32]
    while len(minheap) > 0:
        cost, node = heappop(minheap)
        if cost >= caches[node]:
            continue
        caches[node] = cost
        for nb, dist in edges[node]:
            heappush(minheap, (cost + dist, nb))
    for i in range(len(caches)):
        if caches[i] == 2**32:
            caches[i] = -1
    return caches
