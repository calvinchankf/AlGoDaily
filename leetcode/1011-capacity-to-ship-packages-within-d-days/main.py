from typing import List

"""
    1st: lower bound binary search the number of days
    - be careful that "conveyor belt" means the packages are sent in order

    Time    O(WlogN)
    Space   O(1)
    788 ms, faster than 30.46%
"""


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = 0
        right = 2**31
        while left < right:
            mid = (left + right) // 2
            if self.isPossible(weights, mid, D):
                right = mid
            else:
                left = mid + 1
        return left

    def isPossible(self, nums, cap, D):
        cur = 0
        count = 0
        for x in nums:
            if cur + x > cap:
                count += 1
                cur = 0
            cur += x
            if cur > cap:
                return False
        if cur <= cap:
            count += 1
        else:
            return False
        return count <= D


s = Solution()

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = 5
# # s.isPossible(a, 15, b)
# print(s.shipWithinDays(a, b))

# a = [3, 2, 2, 4, 1, 4]
# b = 3
# print(s.shipWithinDays(a, b))

a = [1, 2, 3, 1, 1]
b = 4
# s.isPossible(a, 2, b)
print(s.shipWithinDays(a, b))
