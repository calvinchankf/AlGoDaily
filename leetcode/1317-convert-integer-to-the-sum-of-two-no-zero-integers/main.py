"""
    1st: brute fore
    - from 1 to n-1, check if there is a pair which both of them contain no zeros in their representation

    Time    O(N)
    Space   O(1)
    24 ms, faster than 88.94% 
"""


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if self.isContainZero(i) == False and self.isContainZero(n-i) == False:
                return [i, n-i]
        return []

    def isContainZero(self, n: int) -> bool:
        s = str(n)
        return "0" in s
