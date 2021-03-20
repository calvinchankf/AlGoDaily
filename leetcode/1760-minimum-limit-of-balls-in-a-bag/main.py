"""
    1st: binary search
    - binary search the bagsize that can be used

    Time    O(NlogN)
    Space   O(1)
    2248 ms, faster than 100.00%
"""


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        total = sum(nums)
        left, right = 1, total
        while left < right:
            mid = (left + right) // 2
            temp = self.check(nums, mid)
            if temp <= maxOperations:
                right = mid
            else:
                left = mid + 1
        return left

    def check(self, nums, bagSize):
        cutCount = 0
        for x in nums:
            if x > bagSize:
                cutCount += math.ceil(x / bagSize) - 1
        return cutCount
