"""
    1st approach: bfs + hashtable
    - similar to lc200

    TIme    O(n)
    Space   O(n)
    84 ms, faster than 19.46%
"""


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        hs = set()
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (i, j) not in hs:
                    self.bfs(board, i, j, hs)
                    count += 1
        return count

    def bfs(self, board, x, y, hs):
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i+1 > len(board) or j < 0 or j+1 > len(board[0]):
                continue
            if (i, j) in hs:
                continue
            hs.add((i, j))
            if board[i][j] == 'X':
                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))


"""
    2nd approach: bfs
    - mutate the board directly

    TIme    O(n)
    Space   O(1)
    84 ms, faster than 19.46%
"""


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    self.bfs(board, i, j)
                    count += 1
        return count

    def bfs(self, board, x, y):
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i+1 > len(board) or j < 0 or j+1 > len(board[0]):
                continue
            if board[i][j] == 'X':
                board[i][j] = '.'
                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))


"""
    2nd approach: dfs
    - mutate the board directly

    TIme    O(n)
    Space   O(1)
    72 ms, faster than 29.19%
"""


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    self.dfs(board, i, j)
                    count += 1
        return count

    def dfs(self, board, i, j):
        if i < 0 or i+1 > len(board) or j < 0 or j+1 > len(board[0]):
            return
        if board[i][j] == 'X':
            board[i][j] = '.'
            self.dfs(board, i-1, j)
            self.dfs(board, i+1, j)
            self.dfs(board, i, j-1)
            self.dfs(board, i, j+1)
