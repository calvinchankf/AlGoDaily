"""
    questions to ask:
    - what if the word is an empty string? return true
    - will the board be empty? yes 
"""

"""
    1st approach: backstracking

    why backtracking works but bfs doesn't work?
    consider this test case
    m = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"],
    ]
    word = ABCESEEEFS

    1. If we do bfs, we marked the S,F,E on the second row as seen 
        before we are going to explore it from the bottom-right E.

    2. backtracking is actually a dfs, if a recursion exits, 
        it 'unseen' the explored coordinates such that we can explore all possibilities.

    Time    O(N * 3^L) N: number of cells, L: length of target word, 3^L instead of 4^L because we dont go backward 
    Space   O(N)
    364 ms, faster than 33.86%
"""


class Solution(object):
    def exist(self, board, word):
        if len(board) == 0 or len(board[0]) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word, idx):
        # if all the characters are checked
        if len(word) == idx:
            return True
        # check boundaries
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return False
        # if can go forward
        if word[idx] != board[i][j]:
            return False
        # first character is found, check the remaining part
        tmp = board[i][j]
        # avoid visit agian
        board[i][j] = "#"
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word, idx+1)\
            or self.dfs(board, i-1, j, word, idx+1)\
            or self.dfs(board, i, j+1, word, idx+1)\
            or self.dfs(board, i, j-1, word, idx+1)
        board[i][j] = tmp
        return res


a = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(Solution().exist(a, "ABCCED"))
print(Solution().exist(a, "SEE"))
print(Solution().exist(a, "ABAB"))


a = [
    ["A", "B", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"],
]
print(Solution().exist(a, "ABCESEEEFS"))

"""
    3rd: backtracking without mutating the array

    Time    O(N * 3^L) N: number of cells, L: length of target word, 3^L instead of 4^L because we dont go backward
    Space   O(N)
    348 ms, faster than 59.46%
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        used = set()
        for i in range(R):
            for j in range(C):
                if self.backtrack(board, i, j, word, used):
                    return True
        return False

    def backtrack(self, board, i, j, word, used):
        R, C = len(board), len(board[0])
        if len(word) == 0:
            return True
        if i < 0 or i == R or j < 0 or j == C:
            return False
        if board[i][j] != word[0]:
            return False
        # to use (i,j)
        key = (i, j)
        if key in used:
            return False
        used.add(key)
        # next recursion
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in dirs:
            if self.backtrack(board, i+di, j+dj, word[1:], used):
                return True
        # backtrack
        used.remove(key)
        return False
