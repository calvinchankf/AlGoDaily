"""
    1st: min-max?
    - store the farthest index along the way
    - if the current index is less than the farthest index, return false

    Time    O(N)
    Space   O(1)
    84 ms, faster than 92.58%
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxIdx = 0
        for i in range(n):
            if i > maxIdx:
                return False
            maxIdx = max(maxIdx, i+nums[i])
        return True
