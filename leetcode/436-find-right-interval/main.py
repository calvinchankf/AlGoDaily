"""
    1st approach: sort + binary search
    - sort the intervals (remember the original index by appending to the end, or create a class)
    - for each input interval, binary search to find the interval[j] which start[j] >= end[i]

    Time    O(nlogn)
    Space   O(n)
    388 ms, faster than 36.55%
"""


class Solution(object):
    def findRightInterval(self, intervals):
        n = len(intervals)
        intvs = []
        for i in range(n):
            x = intervals[i]
            intvs.append((x[0], x[1], i))
        intvs.sort()
        res = []
        for i in range(n):
            s, e = intervals[i]
            j = self.lowerBsearch(intvs, e)
            if j >= 0 and j < n:
                idx = intvs[j][2]
                res.append(idx)
            else:
                res.append(-1)
        return res

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid][0]:
                right = mid
            else:
                left = mid + 1
        return left
