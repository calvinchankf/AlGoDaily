from typing import List

"""
    1st: hashtablesss + BFS
    - define things like directions, candidates...etc beforehand
    - do BFS, to see if the next cell can be connected(accordin to the current direction)

    Time    O(RC)
    Space   O(RC)
    1496 ms, faster than 88.16%
"""


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        directions = {
            1: ['left', 'right'],
            2: ['up', 'down'],
            3: ['left', 'down'],
            4: ['down', 'right'],
            5: ['up', 'left'],
            6: ['up', 'right'],
        }
        didj = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1),
        }
        to_grids = {
            'up': [2, 3, 4],
            'down': [2, 5, 6],
            'left': [1, 4, 6],
            'right': [1, 3, 5],
        }
        counter_dir = {
            '': '',
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left',
        }

        visited = set()
        q = [(0, 0, '')]  # i, j, from direction
        while len(q) > 0:
            i, j, from_dir = q.pop(0)

            # check if visited
            if (i, j) in visited:
                continue
            visited.add((i, j))

            # check if arrive
            if i+1 == len(grid) and j+1 == len(grid[0]):
                return True

            # check the next move following the direction
            symbol = grid[i][j]
            dirs = directions[symbol]  # get ['left', 'right']
            for d in dirs:
                if d == counter_dir[from_dir]:
                    continue
                di, dj = didj[d]
                _i = i + di
                _j = j + dj
                # check boundary
                if _i < 0 or _i == len(grid) or _j < 0 or _j == len(grid[0]):
                    continue

                _symbol = grid[_i][_j]  # 1 -> 6
                if _symbol in to_grids[d]:
                    q.append((_i, _j, d))

        return False


s = Solution()

# true
a = [[2, 4, 3], [6, 5, 2]]
print(s.hasValidPath(a))

# false
a = [[1, 2, 1], [1, 2, 1]]
print(s.hasValidPath(a))

# false
a = [[1, 2, 1], [1, 2, 1]]
print(s.hasValidPath(a))

# true
a = [[1, 1, 1, 1, 1, 1, 3]]
print(s.hasValidPath(a))

# true
a = [[2], [2], [2], [2], [2], [2], [6]]
print(s.hasValidPath(a))

# false
a = [[1, 1, 1, 1, 6], [1, 1, 1, 1, 2], [
    1, 1, 1, 1, 2], [1, 1, 1, 1, 2], [1, 1, 1, 1, 2]]
print(s.hasValidPath(a))

print("-----")

"""
    2nd hashtablesss + recursive DFS
    - basically the same as 1st

    Time    O(RC)
    Space   O(RC)
    1628 ms, faster than 71.67%
"""


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        directions = {
            1: ['left', 'right'],
            2: ['up', 'down'],
            3: ['left', 'down'],
            4: ['down', 'right'],
            5: ['up', 'left'],
            6: ['up', 'right'],
        }
        didj = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1),
        }
        to_grids = {
            'up': [2, 3, 4],
            'down': [2, 5, 6],
            'left': [1, 4, 6],
            'right': [1, 3, 5],
        }
        counter_dir = {
            '': '',
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left',
        }

        visited = set()

        def dfs(i, j, from_dir):
            # print(i, j, from_dir)
            if (i, j) in visited:
                return False
            visited.add((i, j))
            if i+1 == len(grid) and j+1 == len(grid[0]):
                return True
            symbol = grid[i][j]
            dirs = directions[symbol]  # get ['left', 'right']
            is_reached = False
            for d in dirs:
                if d == counter_dir[from_dir]:
                    continue
                di, dj = didj[d]
                _i = i + di
                _j = j + dj
                if _i < 0 or _i == len(grid) or _j < 0 or _j == len(grid[0]):
                    continue

                _symbol = grid[_i][_j]  # 1 -> 6
                if _symbol in to_grids[d]:
                    is_reached = is_reached or dfs(_i, _j, d)
            return is_reached
        return dfs(0, 0, '')


s = Solution()

# true
a = [[2, 4, 3], [6, 5, 2]]
print(s.hasValidPath(a))

# false
a = [[1, 2, 1], [1, 2, 1]]
print(s.hasValidPath(a))

# false
a = [[1, 2, 1], [1, 2, 1]]
print(s.hasValidPath(a))

# true
a = [[1, 1, 1, 1, 1, 1, 3]]
print(s.hasValidPath(a))

# true
a = [[2], [2], [2], [2], [2], [2], [6]]
print(s.hasValidPath(a))

# false
a = [[1, 1, 1, 1, 6], [1, 1, 1, 1, 2], [
    1, 1, 1, 1, 2], [1, 1, 1, 1, 2], [1, 1, 1, 1, 2]]
print(s.hasValidPath(a))
