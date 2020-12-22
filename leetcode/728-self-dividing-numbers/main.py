"""
    1st approach: math
    - for each number, see if it is a self dividing number by using %

    Time    O(nlogn)
    Space   O(n)
    44 ms, faster than 72.25%
"""


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            if self.checkSelfDividing(i):
                res.append(i)
        return res

    def checkSelfDividing(self, num):
        numStr = str(num)
        for c in numStr:
            digit = int(c)
            if digit == 0:
                return False
            elif num % digit != 0:
                return False
        return True
