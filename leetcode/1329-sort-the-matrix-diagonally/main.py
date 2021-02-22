"""
    1st: sort
    - get the left + up boundaries
    - iterate from each boundary diagonally and put the numbers into array
    - sort the array and put that into a temporary array
    - put the numbers back in

    Time    O(NlogN)
    Space   O(N)
    76 ms, faster than 72.33%
"""


class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(mat), len(mat[0])
        heads = []
        for i in range(R):
            heads.append((i, 0))
        for j in range(1, C):
            heads.append((0, j))
        for i, j in heads:
            _i = i
            _j = j
            nums = []
            while _i < R and _j < C:
                nums.append(mat[_i][_j])
                _i += 1
                _j += 1
            nums.sort()
            _i = i
            _j = j
            while _i < R and _j < C:
                mat[_i][_j] = nums.pop(0)
                _i += 1
                _j += 1
        return mat
