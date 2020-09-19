from typing import List
from collections import defaultdict

"""
    1st: hashtable + BFS
    - use a hashtable to store the edges
        e.g. {
            from1: [[to1, cost1], [to2, cost2],....]
            from2: [[to1, cost1], [to2, cost2],....]
            ...
        }
    - the result is the maxCost amongst the paths from root to each of the leaves

    Time    O(N + edges)
    Space   O(edges)
    1436 ms, faster than 75.93%
"""


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        connections = defaultdict(list)
        for i in range(n):
            supervisor = manager[i]
            connections[supervisor].append(i)

        res = 0
        q = [(headID, 0)]
        while len(q) > 0:
            node, time = q.pop(0)
            res = max(res, time)
            if node in connections:
                for child in connections[node]:
                    q.append((child, time + informTime[node]))
        return res


s = Solution()

a = 1
b = 0
c = [-1]
d = [0]
print(s.numOfMinutes(a, b, c, d))

a = 6
b = 2
c = [2, 2, -1, 2, 2, 2]
d = [0, 0, 1, 0, 0, 0]
print(s.numOfMinutes(a, b, c, d))

a = 7
b = 6
c = [1, 2, 3, 4, 5, 6, -1]
d = [0, 6, 5, 4, 3, 2, 1]
print(s.numOfMinutes(a, b, c, d))

a = 15
b = 0
c = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
d = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
print(s.numOfMinutes(a, b, c, d))

a = 4
b = 2
c = [3, 3, -1, 2]
d = [0, 0, 162, 914]
print(s.numOfMinutes(a, b, c, d))

print("-----")


"""
    1st: hashtable + DFS
    - use a hashtable to store the edges
        e.g. {
            from1: [[to1, cost1], [to2, cost2],....]
            from2: [[to1, cost1], [to2, cost2],....]
            ...
        }
    - the result is the maxCost amongst the paths from root to each of the leaves

    Time    O(N + edges)
    Space   O(edges)
    1792 ms, faster than 54.68%
"""


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.connections = defaultdict(list)
        for i in range(n):
            m = manager[i]
            self.connections[m].append([i, 0])

        for key in self.connections:
            t = informTime[key]
            edges = self.connections[key]
            for i in range(len(edges)):
                self.connections[key][i][1] = t

        self.res = 0
        self.dfs(headID, 0)
        return self.res

    def dfs(self, node, cost):
        self.res = max(self.res, cost)
        for child, t in self.connections[node]:
            self.dfs(child, cost + t)


s = Solution()

a = 1
b = 0
c = [-1]
d = [0]
print(s.numOfMinutes(a, b, c, d))

a = 6
b = 2
c = [2, 2, -1, 2, 2, 2]
d = [0, 0, 1, 0, 0, 0]
print(s.numOfMinutes(a, b, c, d))

a = 7
b = 6
c = [1, 2, 3, 4, 5, 6, -1]
d = [0, 6, 5, 4, 3, 2, 1]
print(s.numOfMinutes(a, b, c, d))

a = 15
b = 0
c = [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
d = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
print(s.numOfMinutes(a, b, c, d))

a = 4
b = 2
c = [3, 3, -1, 2]
d = [0, 0, 162, 914]
print(s.numOfMinutes(a, b, c, d))
