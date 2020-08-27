"""
    1st approach: backtracking
    - - similar to lc37, lc51
    - https://www.youtube.com/watch?v=5v6zdfkImms
    - basically try every possisbilities within the safe region
    - for each coordinate, we need to check the whole board to see if it is safe to place a queen

    Time    O(n^4) for each coordinate, we need to check if safe
    Space   O(n^2)
    340 ms, faster than 5.46%
"""


class Solution(object):

    def __init__(self):
        self.result = set()

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        b = Board(n)
        self.backtracking(b, 0, n)
        return len(self.result)

    def backtracking(self, b, row, n):
        if row == n:
            self.result.add(b.stringify())
            return
        for i in range(n):
            if b.isSafe(row, i):
                b.place(row, i)
                self.backtracking(b, row+1, n)
                b.remove(row, i)


class Board(object):
    def __init__(self, n):
        temp = []
        for i in range(n):
            temp.append(n*".")
        self.m = temp
        self.n = n

    def place(self, row, col):
        # basically it is self.m[row][col] = "Q"
        self.m[row] = self.m[row][:col]+"Q"+self.m[row][col+1:]

    def remove(self, row, col):
        # basically it is self.m[row][col] = "."
        self.m[row] = self.m[row][:col]+"."+self.m[row][col+1:]

    def isSafe(self, row, col):
        # check row and col O(n)
        for i in range(self.n):
            if self.m[i][col] == "Q":
                return False
            if self.m[row][i] == "Q":
                return False
        # check diagonal O(n^2)
        for i in range(self.n):
            for j in range(self.n):
                if i+j == row+col or i-j == row-col:
                    if i != row and j != col and self.m[i][j] == "Q":
                        return False
        return True

    def stringify(self):
        # O(n)
        temp = ""
        for i in range(self.n):
            temp += self.m[i]
        return temp


print(Solution().totalNQueens(4))
print(Solution().totalNQueens(5))
print(Solution().totalNQueens(8))
