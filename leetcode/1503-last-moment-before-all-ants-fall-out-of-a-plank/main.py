from typing import List

"""
    1st: min-max
    
    Time    O(N)
    Space   O(1)
    172 ms, faster than 66.67% 
"""


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        toRight = min(right) if len(right) > 0 else n
        toLeft = max(left) if len(left) > 0 else 0
        a = n - toRight
        b = toLeft
        # print(a)
        return max(a, b)


s = Solution()

a = 4
b = [4, 3]
c = [0, 1]
print(s.getLastMoment(a, b, c))

a = 7
b = []
c = [0, 1, 2, 3, 4, 5, 6, 7]
print(s.getLastMoment(a, b, c))

a = 7
b = [0, 1, 2, 3, 4, 5, 6, 7]
c = []
print(s.getLastMoment(a, b, c))

a = 9
b = [5]
c = [4]
print(s.getLastMoment(a, b, c))

a = 6
b = [6]
c = [0]
print(s.getLastMoment(a, b, c))

a = 6
b = [2]
c = [3]
print(s.getLastMoment(a, b, c))

a = 6
b = [3]
c = [2]
print(s.getLastMoment(a, b, c))

a = 1000
b = [0]
c = []
print(s.getLastMoment(a, b, c))
