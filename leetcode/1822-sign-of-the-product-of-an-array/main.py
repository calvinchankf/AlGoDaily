"""
    1st: math

    Time    O(N)
    Space   O(1)
    56 ms, faster than 96.03%
"""


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negativeCount = 0
        for x in nums:
            if x == 0:
                return 0
            if x < 0:
                negativeCount += 1
        if negativeCount % 2 == 0:
            return 1
        return -1
