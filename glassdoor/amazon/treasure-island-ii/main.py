import sys

"""
    You have a map that marks the locations of treasure islands. 
    Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. 
    There are other explorers trying to find the treasure. 
    So you must figure out a shortest route to one of the treasure islands.

    Assume the map area is a two dimensional grid, represented by a matrix of characters. 
    You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. 
    The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. 
    You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. 
    Output the minimum number of steps to get to any of the treasure islands.

    Example:

    Input:
    [['S', 'O', 'O', 'S', 'S'],
    ['D', 'O', 'D', 'O', 'D'],
    ['O', 'O', 'O', 'O', 'X'],
    ['X', 'D', 'D', 'O', 'O'],
    ['X', 'D', 'D', 'D', 'O']]

    Output: 3
    
    Explanation:
    You can start from (0,0), (0, 3) or (0, 4). 
    The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).

    ref:
    - https://leetcode.com/discuss/interview-question/356150
"""


def treasureIslandII(grid):

    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    minSteps = sys.maxsize
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                steps = bfs(grid, i, j)
                minSteps = min(minSteps, steps)
    return minSteps


def bfs(grid, x, y):
    hs = set()
    q = [(x, y, 0)]
    while len(q) > 0:
        i, j, steps = q.pop(0)
        if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
            continue
        if (i, j) in hs:
            continue
        hs.add((i, j))
        if grid[i][j] == 'X':
            return steps
        if grid[i][j] == 'O' or (i == x and j == y):
            q.append((i-1, j, steps+1))
            q.append((i+1, j, steps+1))
            q.append((i, j-1, steps+1))
            q.append((i, j+1, steps+1))
    return sys.maxsize


a = [
    ['S', 'O', 'O', 'S', 'S'],
    ['D', 'O', 'D', 'O', 'D'],
    ['O', 'O', 'O', 'O', 'X'],
    ['X', 'D', 'D', 'O', 'O'],
    ['X', 'D', 'D', 'D', 'O']
]
print(treasureIslandII(a))
