"""
    2nd approach
    - check every cell adjacent cells
    - for each cell, use binary digits to store the next status
    e.g.
    new status | old status
              0|0
              0|1
              1|0
              1|1
    - after calculation, shift the digit to the right to remove the old status

	Time	O(9n) n: row * col
	Space	O(1)
	36 ms, faster than 10.74%
    18apr2019
"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.checkAdjacent(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] >>= 1

    def checkAdjacent(self, board, x, y):
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
                    if x == i and y == j:
                        continue
                    count += board[i][j] & 1

        oldStatus = board[x][y] & 1
        if oldStatus == 0:
            if count == 3:
                board[x][y] = 2  # 1|0
            else:
                board[x][y] = 0  # 0|0
        elif oldStatus == 1:
            if count == 2 or count == 3:
                board[x][y] = 3  # 1|1
            else:
                board[x][y] = 1  # 0|1


a = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
Solution().gameOfLife(a)
print(a)
