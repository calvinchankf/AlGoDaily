

"""
    1st: BFS

    Time    O(RC) but pop(0) takes O(N) so it should be slow
    Space   O(RC)
    856 ms, faster than 33.33%
"""


from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        R, C = len(maze), len(maze[0])
        x, y = entrance
        q = [(x, y, 0, -1, -1)]
        seen = set()
        while len(q) > 0:
            i, j, steps, _i, _j = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                if _i == x and _j == y:
                    continue
                return steps - 1
            if maze[i][j] == '+':
                continue
            key = (i, j)
            if key in seen:
                continue
            seen.add(key)
            q.append((i-1, j, steps + 1, i, j))
            q.append((i+1, j, steps + 1, i, j))
            q.append((i, j-1, steps + 1, i, j))
            q.append((i, j+1, steps + 1, i, j))
        return -1


"""
    2nd: same as 1st but using a double-ended queue

    Time    O(RC)
    Space   O(RC)
    856 ms, faster than 33.33% what???
"""


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        R, C = len(maze), len(maze[0])
        x, y = entrance
        q = deque()
        q.append((x, y, 0, -1, -1))
        seen = set()
        while len(q) > 0:
            i, j, steps, _i, _j = q.popleft()
            if i < 0 or i == R or j < 0 or j == C:
                if _i == x and _j == y:
                    continue
                return steps - 1
            if maze[i][j] == '+':
                continue
            key = (i, j)
            if key in seen:
                continue
            seen.add(key)
            q.append((i-1, j, steps + 1, i, j))
            q.append((i+1, j, steps + 1, i, j))
            q.append((i, j-1, steps + 1, i, j))
            q.append((i, j+1, steps + 1, i, j))
        return -1
