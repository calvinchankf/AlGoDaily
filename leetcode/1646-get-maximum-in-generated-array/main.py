"""
    Time    O(N)
    Space   O(N)
    32 ms, faster than 66.67%
"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 0:
            return 0
        nums = (n+1) * [-1]
        nums[0] = 0
        nums[1] = 1
        res = 1
        for i in range(n+1):
            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[i//2 + 1]
            res = max(res, nums[i])
        return res
