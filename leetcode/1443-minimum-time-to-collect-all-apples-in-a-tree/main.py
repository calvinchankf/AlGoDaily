from typing import List
import sys
from collections import defaultdict

"""
    1st: DFS + hashtable

    Time    O(N)
    Space   O(N)
    752 ms, faster than 63.19%
"""


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        connections = defaultdict(list)
        for a, b in edges:
            connections[a].append(b)
            # connections[b].append(a)
        seen = set()

        def dfs(node):
            if node in seen:
                return 0
            seen.add(node)

            count = 0
            for child in connections[node]:
                count += dfs(child)
            if node == 0:
                return count
            if count > 0:
                return count + 1
            return hasApple[node]
        return dfs(0) * 2


s = Solution()

a = 7
b = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
c = [False, False, True, False, True, True, False]

print(s.minTime(a, b, c))

a = 7
b = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
c = [False, False, True, False, False, True, False]
print(s.minTime(a, b, c))

a = 7
b = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
c = [False, False, False, False, False, False, False]
print(s.minTime(a, b, c))

a = 5
b = [[0, 1], [0, 2], [0, 3], [0, 4]]
c = [False, True, True, True, True]
print(s.minTime(a, b, c))

a = 5
b = [[0, 1], [1, 2], [2, 3], [3, 4]]
c = [False, True, True, True, True]
print(s.minTime(a, b, c))
