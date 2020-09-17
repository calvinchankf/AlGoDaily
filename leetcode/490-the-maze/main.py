"""
    1st approach: BFS
    - similar to lc505, 562
    - if the ball hits the wall, try to roll in 4 directions until the explorations hit the wall
    - only cache the pivot points where we turned(in front of the wall)

    Time    O(RC)
    Space    O(RC)
    268 ms, faster than 73.33%
"""


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        R, C = len(maze), len(maze[0])
        # left, right, up, down
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        ht = {}
        q = []
        q.append((start[0], start[1]))
        while len(q) > 0:
            i, j = q.pop(0)

            # we only care about the stop points
            key = (i, j)
            if key in ht:
                continue
            ht[key] = True

            if i == destination[0] and j == destination[1]:
                return True

            for di, dj in dirs:
                # roll the ball until it hits a wall
                _i = i
                _j = j
                while 0 <= _i+di < R and 0 <= _j+dj < C and maze[_i+di][_j+dj] == 0:
                    _i += di
                    _j += dj
                q.append((_i, _j))
        return False


a = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

print("----------")

"""
    2nd approach: DFS
    - similar to lc505, 562
    - if the ball hits the wall, try to roll in 4 directions until the explorations hit the wall
    - only cache the pivot points where we turned(in front of the wall)

    Time    O(RC)
    Space    O(RC)
    272 ms, faster than 48.96%
"""


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # left, right, up, down
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        # destination
        destI, destJ = destination[0], destination[1]
        visited = set()

        def dfs(i, j):
            if i == destI and j == destJ:
                return True
            for di, dj in dirs:
                # roll the ball until it hits a wall
                _i = i
                _j = j
                while 0 <= _i+di < len(maze) and 0 <= _j+dj < len(maze[0]) and maze[_i+di][_j+dj] == 0:
                    _i += di
                    _j += dj
                # check if the new starting position has been visited
                if (_i, _j) in visited:
                    continue
                visited.add((_i, _j))
                if dfs(_i, _j):
                    return True
            return False
        return dfs(start[0], start[1])


a = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

a = [
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
]
b = [0, 4]
c = [4, 4]
print(Solution().hasPath(a, b, c))

"""
    3rd: backtracking

    Time    O(RC)
    Space   O(RC)
    292 ms, faster than 87.85%
"""


class Solution:
    def hasPath(self, maze, start, destination):
        if len(maze) == 0 or len(maze[0]) == 0:
            return False

        hs = set()

        def dfs(i, j):

            if (i, j) in hs:
                return False
            hs.add((i, j))

            if i == destination[0] and j == destination[1]:
                return True
            cands = []

            _i = i
            while _i-1 >= 0 and maze[_i-1][j] == 0:
                _i -= 1
            cands.append((_i, j))

            _i = i
            while _i+1 < len(maze) and maze[_i+1][j] == 0:
                _i += 1
            cands.append((_i, j))

            _j = j
            while _j-1 >= 0 and maze[i][_j-1] == 0:
                _j -= 1
            cands.append((i, _j))

            _j = j
            while _j+1 < len(maze[0]) and maze[i][_j+1] == 0:
                _j += 1
            cands.append((i, _j))

            for x, y in cands:
                b = dfs(x, y)
                if b:
                    return True

            # unlike a typical backtracking, we dont remove
            # because if this point cannot reach to the endpoint, then it does wherever it came from
            # hs.remove((i, j))
            return False

        return dfs(start[0], start[1])
