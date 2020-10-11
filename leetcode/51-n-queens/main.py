"""
    1st approach: backtracking
    - similar to lc37, lc52 
    - https://www.youtube.com/watch?v=5v6zdfkImms
    - basically try every possisbilities within the safe region
    - for each coordinate, we need to check the whole board to see if it is safe to place a queen

    Time    O(N! NN)
    Space   O(N)
    348 ms, faster than 6.62%
"""


class Solution(object):

    def __init__(self):
        self.result = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        b = Board(n)
        self.backtracking(b, 0, n)
        return self.result

    def backtracking(self, b, row, n):
        if row == n:
            self.result.append(b.clone())
            return
        for i in range(n):
            if b.isSafe(row, i):
                b.place(row, i)
                x = self.backtracking(b, row+1, n)
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

    def clone(self):
        # O(n)
        temp = []
        for i in range(self.n):
            temp.append(self.m[i])
        return temp

s = Solution()
print(s.solveNQueens(4))
print(s.solveNQueens(5))
print("-----")

"""
    2nd: backtracking with hashtable
    - optimize the 1st with a hashtable by storing the used rol, col, diag, antidiag indices

    Time    O(N!)
    Space   O(N)
    156 ms, faster than 24.22%
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rowHt = set()
        colHt = set()
        diagHt = set()
        antiDiagHt = set()
        
        self.res = {}
        board = self.getBoard(n)
        self.dfs(n, 0, rowHt, colHt, diagHt, antiDiagHt, board)
        
        final = []
        for key in self.res:
            final.append(self.res[key])
        return final
    
    def dfs(self, n, i, rowHt, colHt, diagHt, antiDiagHt, board):
        if i == n:
            key = self.getBoardKey(board)
            val = self.getBoardResult(board)
            self.res[key] = val
            return
        
        for j in range(n):
            diagKey = i - j
            antiDiagKey = i + j
            if i not in rowHt\
                and j not in colHt\
                and diagKey not in diagHt\
                and antiDiagKey not in antiDiagHt:
                
                rowHt.add(i)
                colHt.add(j)
                diagHt.add(diagKey)
                antiDiagHt.add(antiDiagKey)
                
                clone = self.copyBoard(board)
                clone[i][j] = 'Q'
                
                self.dfs(n, i+1, rowHt, colHt, diagHt, antiDiagHt, clone)
                
                rowHt.remove(i)
                colHt.remove(j)
                diagHt.remove(diagKey)
                antiDiagHt.remove(antiDiagKey)
    
    def getBoard(self, n):
        board = []
        for _ in range(n):
            board.append(n * ['.'])
        return board
                
    def copyBoard(self, board):
        n = len(board)
        clone = self.getBoard(n)
        for i in range(n):
            for j in range(n):
                clone[i][j] = board[i][j]
        return clone
    
    def getBoardKey(self, board):
        n = len(board)
        res = ''
        for i in range(n):
            for j in range(n):
                res += board[i][j]
        return res
    
    def getBoardResult(self, board):
        n = len(board)
        res = []
        for i in range(n):
            s = ''.join(board[i])
            res.append(s)
        return res

s = Solution()
print(s.solveNQueens(4))
print(s.solveNQueens(5))
print("-----")