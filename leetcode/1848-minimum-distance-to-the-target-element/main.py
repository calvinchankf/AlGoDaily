"""
    1st: array

    Time    O(N)
    Space   O(1)
    56 ms, faster than 89.70%
"""


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = 2**32
        for i in range(len(nums)):
            if nums[i] == target:
                res = min(res, abs(i - start))
        return res
