"""
    1st: sort + binary search
    - sort the points by x
    - for every query, check the range of points between the lower bound and the upper bound

    Time    O(PlogP + NlogP)
    Space   O(N)
    1900 ms, faster than 100.00%
"""


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points.sort(key=lambda el: (el[0], el[1]))
        n = len(queries)
        res = n * [0]
        for i in range(n):
            x, y, r = queries[i]
            left = self.lowerBsearch(points, x-r)
            right = self.upperBsearch(points, x+r)
            for j in range(left, right):
                _x, _y = points[j]
                if (_x - x)**2 + (_y - y)**2 <= r**2:
                    res[i] += 1
        return res

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid][0]:
                right = mid
            else:
                left = mid + 1
        return left

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid][0]:
                left = mid + 1
            else:
                right = mid
        return right
