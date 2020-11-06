"""
    1st: prefix sum on each row

    Time of init()      O(RC)
    Time of sumRage()   O(R)
    Space               O(RC)
    212 ms, faster than 6.65%
"""
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.cache = []
        for nums in matrix:
            pfs = 0
            pfss = []
            for x in nums:
                pfs += x
                pfss.append(pfs)
            self.cache.append(pfss)
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = 0
        for i in range(row1, row2 + 1):
            s = self.cache[i][col2]
            if col1-1 >= 0:
                s -= self.cache[i][col1-1]
            total += s
        return total


"""
    2nd: prefix sum + calculation

     a |  b  |
    ___|_____|__
       |     |
     c |  d  |
    ___|_____|__
       |     |
    
    Sum(ABCD) = Sum(OD) − Sum(OB) − Sum(OC) + Sum(OA)

    see ./idea.png

    Time of init()      O(RC)
    Time of sumRage()   O(1)
    Space               O(RC)
    96 ms, faster than 55.66%
"""

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        R, C = len(matrix), len(matrix[0])
        cache = [C * [0] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                top = cache[i-1][j] if i-1 >= 0 else 0
                left = cache[i][j-1] if j-1 >= 0 else 0
                topLeft = cache[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
                cache[i][j] = matrix[i][j] + top + left - topLeft
        self.cache = cache
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.cache:
            return 0
        top = self.cache[row1-1][col2] if row1-1 >= 0 else 0
        left = self.cache[row2][col1-1] if col1-1 >= 0 else 0
        topLeft = self.cache[row1-1][col1-1] if row1-1 >= 0 and col1-1 >= 0 else 0
        return self.cache[row2][col2] - top - left + topLeft