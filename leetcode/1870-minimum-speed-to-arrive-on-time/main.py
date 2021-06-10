"""
    1st: lower bound binary search

    Time    O(N * log(2**32))
    Space   O(1)
    5192 ms, faster than 40.00%
"""


class Solution:
    def minSpeedOnTime(self, dists: List[int], hour: float) -> int:
        left = 1
        right = 2**32
        while left < right:
            mid = (left + right)//2
            total = self.getTotal(dists, mid)
            if total <= hour:
                right = mid
            else:
                left = mid + 1
        if left == 2**32:
            return -1
        return left

    def getTotal(self, dists, speed):
        n = len(dists)
        total = 0
        for i in range(n-1):
            total += math.ceil(dists[i] / speed)
        return total + dists[-1] / speed
