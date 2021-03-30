"""
    lc1761

    https://leetcode.com/discuss/interview-question/934203/Amazon-or-OA-2020-or-New-question-Shopping-Patterns-or-Experienced
    https://aonecode.com/amazon-online-assessment-shopping-patterns

    Amazon is trying to understand customer shopping patterns and offer items that are regularly bought together to new customers. 
    Each item that has been bought together can be represented as an undirected graph where edges join often bundled products. A group of n products is uniquely numbered from 1 of product_nodes. A trio is defined as a group of three related products that all connected by an edge. Trios are scored by counting the number of related products outside of the trio, this is referred as a product sum.

    Given product relation data, determine the minimum product sum for all trios of related products in the group. 
    If no such trio exists, return -1.

    Example:
    products_nodes  = 6
    products_edges  = 6
    products_from   = [1,2,2,3,4,5]
    products_to     = [2,4,5,5,5,6]

    The relationship is like:
    1 - 2 - 4
          \ |
        3 - 5 - 6
    
    A graph of n = 6 products where the only trio of related products is (2, 4, 5).

    Node 2 has 1 non trio neighbour
    Node 4 has 0 non trio neighbour
    Node 5 has 2 non trio neighbour
    So for the trio (2, 4, 5), the total product score is 1 + 0 + 2 = 3
"""


def f(product_nodes, product_edges, product_from, product_to):
    """
        Approach:
        For every node that has more than 2 neighbours, 
        check every pair of its neighbours to see if there is an intersection

        V: number of vertice, E: number of edges

        Time    O(VEE) I try all the neighbors pairs of every node
        Space   O(VE)
    """
    n = product_nodes
    edges = []
    for i in range(len(product_from)):
        edges.append((product_from[i], product_to[i]))

    isConnected = []
    indegrees = []
    for i in range(n):
        indegrees.append(0)
        isConnected.append(n * [False])
    for _u, _v in edges:
        u = _u - 1
        v = _v - 1
        isConnected[u][v] = True
        isConnected[v][u] = True
        indegrees[u] += 1
        indegrees[v] += 1
    res = 2**32
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if isConnected[i][j] and isConnected[j][k] and isConnected[k][i]:
                    res = min(res, indegrees[i] +
                              indegrees[j] + indegrees[k] - 6)
    if res == 2**32:
        return -1
    return res


a = 6
b = 6
c = [1, 2, 2, 3, 4, 5]
d = [2, 4, 5, 5, 5, 6]
print(f(a, b, c, d))

a = 5
b = 6
c = [1, 1, 2, 2, 3, 4]
d = [2, 3, 3, 4, 4, 5]
print(f(a, b, c, d))

"""
    my test:

    1 - 2
    | \ |
    4   3 - 5 - 6
              \ |
                7

    For trio 123, score = 2
    For trio 567, score = 1
"""
a = 7
b = 8
c = [1, 1, 1, 2, 3, 5, 6, 7]
d = [4, 2, 3, 3, 5, 6, 7, 5]
print(f(a, b, c, d))
