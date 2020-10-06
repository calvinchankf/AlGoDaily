import sys

"""
    1st: BFS + hashtable

    Time    O(RCK) every "cell and remaining K" would only be visited once 
    Space   O(RCK)
    1748 ms, faster than 5.21%
"""


class Solution(object):
    def shortestPath(self, grid, k):
        R, C = len(grid), len(grid[0])
        seen = set()
        q = [(0, 0, 0, k)]
        while len(q) > 0:
            i, j, steps, remainingK = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue

            # if this is an obstacle, break it
            if grid[i][j] == 1:
                remainingK -= 1
            if remainingK < 0:
                continue

            # the first one must be the shortest
            if i+1 == R and j+1 == C:
                return steps

            # avoid redundant visits
            key = (i, j, remainingK)
            if key in seen:
                continue
            seen.add(key)

            # traverse
            q.append((i-1, j, steps+1, remainingK))
            q.append((i+1, j, steps+1, remainingK))
            q.append((i, j-1, steps+1, remainingK))
            q.append((i, j+1, steps+1, remainingK))

        return -1


s = Solution()

a = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
b = 1
print(s.shortestPath(a, b))

a = [[0, 1, 1], [1, 1, 1], [1, 0, 0]]
b = 1
print(s.shortestPath(a, b))

a = [[0, 0],
     [1, 0],
     [1, 0],
     [1, 0],
     [1, 0],
     [1, 0],
     [0, 0],
     [0, 1],
     [0, 1],
     [0, 1],
     [0, 0],
     [1, 0],
     [1, 0],
     [0, 0]]
b = 4
print(s.shortestPath(a, b))

a = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
b = 0
print(s.shortestPath(a, b))

a = [
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 0],
]
b = 1
print(s.shortestPath(a, b))

a = [
    [0, 0],
    [0, 1],
    [1, 1],
    [0, 0],
]
b = 1
print(s.shortestPath(a, b))

print("-----")
