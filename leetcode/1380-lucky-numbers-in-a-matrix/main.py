from sys import maxsize

"""
    1st: hashtable

    Time    O(2RC)
    Space   O(RC)
    144 ms, faster than 51.91% 
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        hs = set()
        for i in range(len(matrix)):
            min_j = -1
            min_num = maxsize
            for j in range(len(matrix[0])):
                if matrix[i][j] < min_num:
                    min_num = matrix[i][j]
                    min_j = j
            hs.add((i, min_j))
        res = []
        for j in range(len(matrix[0])):
            max_i = -1
            max_num = -maxsize
            for i in range(len(matrix)):
                if matrix[i][j] > max_num:
                    max_num = matrix[i][j]
                    max_i = i
            if (max_i, j) in hs:
                res.append(matrix[max_i][j])
        return res