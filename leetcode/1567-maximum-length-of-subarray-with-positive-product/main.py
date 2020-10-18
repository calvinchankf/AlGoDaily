"""
    1st: dp
    - similar to lc152

    Time    O(N)
    Space   O(1)
    1012 ms, faster than 100.00%
"""


class Solution(object):
    def getMaxLen(self, nums):
        negPLen = 0
        posPLen = 0
        res = 0
        for num in nums:
            if num > 0:
                posPLen += 1
                negPLen = negPLen + 1 if negPLen > 0 else 0
            elif num < 0:
                temp = posPLen
                posPLen = negPLen + 1 if negPLen > 0 else 0
                negPLen = temp+1
            else:
                posPLen = 0
                negPLen = 0
            res = max(res, posPLen)
        return res


s = Solution()

a = [1, -2, -3, 4]
print(s.getMaxLen(a))

a = [0, 1, -2, -3, -4]
print(s.getMaxLen(a))

a = [-1, -2, -3, 0, 1]
print(s.getMaxLen(a))

a = [-1, 2]
print(s.getMaxLen(a))

a = [1, 2, 3, 5, -6, 4, 0, 10]
print(s.getMaxLen(a))

a = [1]
print(s.getMaxLen(a))

a = [-1]
print(s.getMaxLen(a))

# 6
a = [-16, 0, -5, 2, 2, -13, 11, 8]
print(s.getMaxLen(a))
