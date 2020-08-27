"""
    There's an undirected connected graph with n nodes labeled 1..n.
    But some of the edges has been broken disconnecting the graph. 
    Find the minimum cost to repair the edges so that all the nodes are once again accessible from each other.

    Input:

    n: an int representing the total number of nodes.
    edges: a list of integer pair representing the nodes connected by an edge.
    edgesToRepair: a list where each element is a triplet representing the pair of nodes between which an edge is currently broken and the cost of repearing that edge
               e.g. [1, 2, 12] means to repear an edge between nodes 1 and 2, the cost would be 12
    
    ----------------------------------------------------------
    Example 1:

    Input: n = 5
    edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
    
    Output: 20
    
    Explanation:
    There are 3 connected components due to broken edges: [1], [2, 3] and [4, 5].
    We can connect these components into a single component by repearing the edges between nodes 1 and 2, and nodes 1 and 5 at a minimum cost 12 + 8 = 20.
    ----------------------------------------------------------
    Example 2:
    
    Input: n = 6
    edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]]
    edgesToRepair = [[1, 6, 410], [2, 4, 800]]
    
    Output: 410
    ----------------------------------------------------------
    Example 3:
    
    Input: n = 6
    edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]]
    edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
    
    Output: 79

    ref:
    - https://leetcode.com/discuss/interview-question/357310
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


def minCostToRepair(n, edges, edgesToRepair):
    # prepare to un-consider edgesToRepair
    brokens = set()
    for a, b, c in edgesToRepair:
        brokens.add((a, b))
    # group the edges
    uf = UnionFind(n)
    for a, b in edges:
        if (a, b) in brokens or (b, a) in brokens:
            continue
        uf.union(a, b)
    res = 0
    # see if a and b are connected for every edgesToRepair
    edgesToRepair = sorted(edgesToRepair, key=lambda x: x[2])
    for a, b, c in edgesToRepair:
        rootA = uf.find(a)
        rootB = uf.find(b)
        if rootA != rootB:
            uf.union(a, b)
            res += c
    # we cannot connect all of them
    if uf.count > 1:
        return -1
    return res


a = 5
b = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
c = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
print(minCostToRepair(a, b, c))

a = 6
b = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]]
c = [[1, 6, 410], [2, 4, 800]]
print(minCostToRepair(a, b, c))

a = 6
b = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]]
c = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
print(minCostToRepair(a, b, c))
