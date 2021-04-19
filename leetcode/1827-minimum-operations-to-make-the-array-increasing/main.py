"""
    1st: math
    - get the diff btw the current and the previous element,
        add the diff to the current element

    Time    O(N)
    Space   O(1)
    124 ms, faster than 100.00%
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            diff = nums[i-1] - nums[i]
            if diff < 0:
                continue
            inc = diff + 1
            ans += inc
            nums[i] += inc
        return ans
