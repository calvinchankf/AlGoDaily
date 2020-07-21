from typing import List
from collections import defaultdict

"""
    1st: backtracking + hashtable
    - similar to lc51, lc52
    - the basic idea is to try every possibility with recursion (with backtracking)
    - use 3 hashtables
        - to save the used numbers on each row
        - to save the used numbers on each column
        - to save the used numbers on each 3x3 grid
    - in each recursive function, gather the possibilites that we can use by ignoring the numbers in hashtables
    - backtrack if we dont have candicates if we are still unfilled cells
    - return True if we reach to the end

    Time of brute force   O(9^N) -> O(9^81) Total at most 81 cells. For each cell, there are 9 possbilities
    Time of backtracking  O((9!)^9)         On each row, there are 
                                            - not more than 9 possibilities for the first empty cell to put, 
                                            - not more than 9 x 8 for the second one, 
                                            - not more than 9 x 8 x 7 for the third one,...etc
    Space    O(81)
    196 ms, faster than 73.90%
"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        rowHt = defaultdict(set)    # record the used numbers in every row
        colHt = defaultdict(set)    # record the used numbers in every column
        gridHt = defaultdict(set)   # 3x3: (0,0), (0,3), (0,6), (3,0), (3,3)...

        # 1. clone the original board
        # 2. put the filled cells in hashtables accordingly
        original = []
        for i in range(len(board)):
            temp = []
            for j in range(len(board[0])):
                x = board[i][j]
                temp.append(x)
                if x != '.':
                    rowHt[i].add(x)
                    colHt[j].add(x)
                    gridHt[i//3*3, j//3*3].add(x)
            original.append(temp)

        def backtrack(i, j):
            if i == R and j == 0:
                return True

            # if (i,j) in the original board, try the next cell
            if original[i][j] != '.':
                b = False
                if j+1 < C:
                    b = backtrack(i, j+1)
                else:
                    b = backtrack(i+1, 0)
                return b

            # merge the hashtable for specific i, j, 3x3 key
            key = i//3*3, j//3*3
            s = set()
            s |= rowHt[i]
            s |= colHt[j]
            s |= gridHt[key]

            # we only consider the numbers which hasnt been used
            cands = []
            for num in range(1, 10):
                x = str(num)
                if x not in s:
                    cands.append(x)

            # try all possibilities
            for cand in cands:
                rowHt[i].add(cand)
                colHt[j].add(cand)
                gridHt[key].add(cand)
                board[i][j] = cand
                b = 0
                if j+1 < C:
                    b = backtrack(i, j+1)
                else:
                    b = backtrack(i+1, 0)
                if b:
                    return True
                # False means we cannot reach to the end, therefore backtrack the candidate
                rowHt[i].remove(cand)
                colHt[j].remove(cand)
                gridHt[key].remove(cand)
                board[i][j] = '.'
            return False

        backtrack(0, 0)


s = Solution()

a = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s.solveSudoku(a)
print(a)

""" answer
[['5', '3', '4', '6', '7', '2', '9', '1', '8'],
 ['6', '8', '2', '1', '9', '5', '4', '3', '7'],
 ['1', '9', '8', '3', '4', '7', '5', '6', '2'],
 ['8', '1', '9', '2', '6', '4', '7', '5', '3'],
 ['4', '2', '7', '8', '5', '3', '6', '9', '1'],
 ['7', '5', '3', '9', '2', '8', '1', '4', '6'],
 ['9', '6', '5', '7', '3', '1', '2', '8', '4'],
 ['3', '7', '6', '4', '1', '9', '8', '2', '5'],
 ['2', '4', '1', '5', '8', '6', '3', '7', '9']]
"""
