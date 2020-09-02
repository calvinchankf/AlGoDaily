import sys

"""
    Given a 2D grid, each cell is either a zombie 1 or a human 0. 
    Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. 
    Find out how many hours does it take to infect all humans?

    Input:
    [[0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0]]

    Output: 2

    Explanation:
    At the end of the 1st hour, the status of the grid:
    [[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1]]

    At the end of the 2nd hour, the status of the grid:
    [[1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]]

    ref:
    - https://leetcode.com/discuss/interview-question/411357/
"""


def zombieInMatrix(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    R, C = len(grid), len(grid[0])
    days = []
    for _ in range(R):
        days.append(C * [sys.maxsize])

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                bfs(grid, days, i, j)

    minDays = 0
    for i in range(R):
        for j in range(C):
            minDays = max(minDays, days[i][j])
    return minDays


def bfs(grid, days, x, y):
    R, C = len(grid), len(grid[0])
    q = [(x, y, 0)]
    while len(q) > 0:
        i, j, steps = q.pop(0)
        if i < 0 or i == R or j < 0 or j == C:
            continue
        if steps >= days[i][j]:
            continue
        days[i][j] = steps
        if grid[i][j] == 0 or (i == x and j == y):
            q.append((i-1, j, steps + 1))
            q.append((i+1, j, steps + 1))
            q.append((i, j-1, steps + 1))
            q.append((i, j+1, steps + 1))


a = [
    [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
]
print(zombieInMatrix(a))
