"""
    1st: array
    - calculate the indeces diff between every pair of 1
    - should be EASY

    Time    O(N)
    Space   O(1)
    576 ms, faster than 97.88%
"""


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastIdx = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if lastIdx == -1:
                    lastIdx = i
                else:
                    diff = i - lastIdx - 1
                    if diff < k:
                        return False
                    lastIdx = i
        return True
