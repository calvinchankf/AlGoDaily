"""
    1st: better brute-force
    - for each cell > 0, explore to the right and the the bottom to see if we can find a row or/and a column to crush
    - if there is a range of cells should be crushed, update their value to be cel[i][j] += 2000, therefore we use mode(%) for row/col check 
    - to reduce redandant calculation, store the range of a pendingRow(rightMax) and the range of a pendingColumn(bottomMax) and check if the current cell is within the ranges when we iterate the board

    Time    k * O( RC * (R+C))
    Space   O(max(R, C))
    412 ms, faster than 5.14%
"""
class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        while True:
            shouldCrush = False
            rightMax = [-1, -1, -1] # i, j from, j to+1
            bottomMax = [-1, -1, -1] # j, i from, i to+1
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != 0:
                        if not (i == rightMax[0] and rightMax[1] <= j < rightMax[2]):
                            rightCount = self.explore2Right(board, i, j)
                            if rightCount >= 3:
                                shouldCrush = True
                                rightMax = [i, j, j+rightCount]
                        if not (j == bottomMax[0] and bottomMax[1] <= i < bottomMax[2]):
                            bottomCount = self.explore2Bottom(board, i, j)
                            if bottomCount >= 3:
                                shouldCrush = True
                                bottomMax = [j, i, i+bottomCount]
            if shouldCrush:
                self.crush(board)
            else:
                break
        return board

    def explore2Right(self, board, i, j):
        target = board[i][j]%2000
        j2 = j
        while j2 < len(board[0]):
            if board[i][j2] % 2000 == target:
                j2 += 1
            else:
                break
        count = j2 - j
        if count >= 3:
            for idx in range(count):
                board[i][j+idx] += 2000
        return count

    def explore2Bottom(self, board, i, j):
        target = board[i][j]%2000
        i2 = i
        while i2 < len(board):
            if board[i2][j] % 2000 == target:
                i2 += 1
            else:
                break
        count = i2 - i
        if count >= 3:
            for idx in range(count):
                board[i+idx][j] += 2000
        return count

    def crush(self, board):
        for j in range(len(board[0])):
            temp = []
            for i in range(len(board)-1, -1, -1):
                if board[i][j] <= 2000:
                    temp.append(board[i][j])
            idx = 0
            for i in range(len(board)-1, -1, -1):
                if idx < len(temp):
                    board[i][j] = temp[idx]
                    idx += 1
                else:
                    board[i][j] = 0

s = Solution()

a = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
s.candyCrush(a)