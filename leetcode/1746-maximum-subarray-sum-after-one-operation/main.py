"""
    1st: 2 array min max
    - similar to lc915

    Time    O(3N)
    Space   O(3N)
    1300 ms, faster than 100.00%
"""


class Solution(object):
    def maxSumAfterOperation(self, nums):
        if len(nums) == 0:
            return 0
        n = len(nums)
        forward = []
        cur = -(2**32)
        for i in range(n):
            cur = max(cur+nums[i], nums[i])
            forward.append(cur)

        backward = []
        cur = -(2**32)
        for i in range(n-1, -1, -1):
            cur = max(cur+nums[i], nums[i])
            backward.append(cur)
        backward.reverse()

        res = -(2**32)
        for i in range(n):
            x = nums[i]**2
            if i-1 >= 0 and forward[i-1] >= 0:
                x += forward[i-1]
            if i+1 < n and backward[i+1] >= 0:
                x += backward[i+1]
            res = max(res, x)
        return res
