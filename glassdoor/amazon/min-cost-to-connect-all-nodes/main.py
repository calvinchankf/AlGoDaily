"""
    Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. 
    The i-th edge connects nodes edges[i][0] and edges[i][1] together. 
    Your task is to augment this set of edges with additional edges to connect all the nodes. 
    Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

    Input:

    n: an int representing the total number of nodes.
    edges: a list of integer pair representing the nodes already connected by an edge.
    newEdges: a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, 
            e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5.
    
    Example 1:
    
    Input: n = 6
    edges = [[1, 4], [4, 5], [2, 3]]
    newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
    
    Output: 7
    
    Explanation:
    There are 3 connected components [1, 4, 5], [2, 3] and [6].
    We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.

    ref:
    - https://leetcode.com/discuss/interview-question/356981
"""


class UnionFind(object):
    def __init__(self, N):
        self.count = N
        self.ids = {}
        self.caps = {}
        for i in range(1, N+1):
            self.ids[i] = i
            self.caps[i] = 1

    def getCount(self):
        return self.count

    def find(self, key):
        # loop to find to ultimate root
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1


def minCostToConnect(n, edges, newEdges):
    # group the edges
    uf = UnionFind(n)
    for a, b in edges:
        uf.union(a, b)
    res = 0
    # see if a and b are connected for every newEdge
    newEdges = sorted(newEdges, key=lambda x: x[2])
    for a, b, c in newEdges:
        rootA = uf.find(a)
        rootB = uf.find(b)
        if rootA != rootB:
            uf.union(a, b)
            res += c
    # we cannot connect all of them
    if uf.count > 1:
        return -1
    return res


a = 6
b = [[1, 4], [4, 5], [2, 3]]
c = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
print(minCostToConnect(a, b, c))
