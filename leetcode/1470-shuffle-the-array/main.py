"""
    1st: array

    Time    O(N)
    Space   O(N)
    76 ms, faster than 72.28%
"""


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(len(nums)//2):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
