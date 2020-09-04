import sys
from collections import defaultdict

""" 
    question: https://leetcode.com/discuss/interview-question/436073/

    You are given an undirected connected graph. 
    An articulation point (or cut vertex) is defined as a vertex which, 
    when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). 
    The task is to find all articulation points in the given graph.

    Input:
    The input to the function/method consists of three arguments:

    numNodes, an integer representing the number of nodes in the graph.
    numEdges, an integer representing the number of edges in the graph.
    edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
    Output:
    Return a list of integers representing the critical nodes.

    Example:

    Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
"""


"""
    1st: brute force
    - exclude each node
    - traverse the graph to see if all connected. If not, that excluded node is critical

    Time    O(E + N^2)
    Space   O(N)
"""


class Solution(object):
    def findCriticalNodes(self, n, edges):
        connections = defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)

        res = []
        for i in range(n):
            q = []
            if i < n-1:
                q.append(i+1)
            else:
                q.append(0)
            seen = set()
            while len(q) > 0:
                node = q.pop(0)
                if node in seen:
                    continue
                seen.add(node)
                if node == i:
                    continue
                for nextNode in connections[node]:
                    q.append(nextNode)
            if len(seen) < n:
                res.append(i)

        return res


s = Solution()

a = 7
b = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
print(s.findCriticalNodes(a, b))

a = 6
b = [[0, 1], [0, 3], [1, 2], [3, 2], [2, 5], [2, 4], [4, 5]]
print(s.findCriticalNodes(a, b))

a = 6
b = [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [3, 5], [4, 5]]
print(s.findCriticalNodes(a, b))

print("-----")

"""
    2nd: Tarjan
    - find the strongly connected components(group of nodes)
    - each of a critical node is either
        - the point to enter a strongly connected component
        - the point to connect a list of leak components

    ref:
    - 
    - https://www.youtube.com/watch?v=aZXi1unBdJA
    - https://www.youtube.com/watch?v=2kREIkF9UAs
    - https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/ArticulationPoint.java

    Time    O(E + N)
    Space   O(N)
"""


class Solution(object):
    def findCriticalNodes(self, n, edges):
        connections = defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)

        self.curStep = 0
        lowestTimes = [sys.maxsize for i in range(n)]
        visitedTimes = {}
        self.res = []
        self.dfs(connections, None, 0, visitedTimes, lowestTimes)
        return self.res

    def dfs(self, connections, prevNode, curNode, visitedTimes, lowestTimes):
        visitedTimes[curNode] = self.curStep
        lowestTimes[curNode] = self.curStep
        self.curStep += 1
        for nextNode in connections[curNode]:
            if nextNode not in visitedTimes:
                self.dfs(
                    connections, curNode, nextNode, visitedTimes, lowestTimes
                )
                lowestTimes[curNode] = min(
                    lowestTimes[curNode], lowestTimes[nextNode]
                )
                # explanation of `>=`:
                # - `>` means we must reach next node(not a cycle) from curNode, so curNode is critical
                # - `=` means we must enter a cycle from curNode, so curNode is critical(the reason is all nodes in a cycle have the same lowestTime)
                if lowestTimes[nextNode] >= visitedTimes[curNode] and prevNode != None:
                    self.res.append(curNode)
            else:
                lowestTimes[curNode] = min(
                    lowestTimes[curNode], visitedTimes[nextNode]
                )


s = Solution()

a = 7
b = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
print(s.findCriticalNodes(a, b))

a = 6
b = [[0, 1], [0, 3], [1, 2], [3, 2], [2, 5], [2, 4], [4, 5]]
print(s.findCriticalNodes(a, b))

a = 6
b = [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [3, 5], [4, 5]]
print(s.findCriticalNodes(a, b))
