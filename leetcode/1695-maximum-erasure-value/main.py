from collections import Counter
"""
    2 pointers (sliding window)
    - similar to lc3

    Time    O(N)
    Space   O(N)
    1728 ms, faster than 24.96%
"""


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = Counter()
        j = 0
        res = -(2**32)
        total = 0
        for i in range(len(nums)):
            x = nums[i]
            window[x] += 1
            total += x
            while window[x] > 1:
                left = nums[j]
                j += 1
                window[left] -= 1
                total -= left
                if window[left] == 0:
                    del window[left]
            res = max(res, total)
        return res
