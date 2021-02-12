"""
    greedy?
    - for every ball, go down if it is not stuck with it neighbours

    Time    O(RC)
    Space   O(C)
    196 ms, faster than 94.29% 
"""


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        R = len(grid)
        C = len(grid[0])
        res = C * [-1]
        for idx in range(C):
            i, j = 0, idx
            shouldGoDown = True
            while i != R:
                if grid[i][j] == 1:
                    if j+1 == C or grid[i][j+1] == -1:
                        shouldGoDown = False
                        break
                    j += 1
                if grid[i][j] == -1:
                    if j == 0 or grid[i][j-1] == 1:
                        shouldGoDown = False
                        break
                    j -= 1
                i += 1
            if shouldGoDown:
                res[idx] = j
        return res
