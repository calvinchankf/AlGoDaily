from typing import List

"""
    1st: common upper bound binary search
    Time    O(RC) <- reversing each row takes linear time O(N)
    Space   O(C)
    128 ms beats 66.06%
"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            arr = grid[i]
            r = arr[::-1]
            idx = self.upperBsearch(r, -1)
            if idx > 0:
                count += idx
        return count

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right


s = Solution()

a = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(s.countNegatives(a))

print('---')


"""
    2nd: descending list upper bound binary search
    Time    O(RlogC) <- binary search takes O(logC)
    Space   O(C)
    124 ms, faster than 85.44%
"""


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            arr = grid[i]
            idx = self.upperBsearch(arr, 0)
            count = len(arr) - idx - 1
            if count > 0:
                res += count
        return res

    def upperBsearch(self, nums, target):
        left = -1
        right = len(nums)-1
        while left < right:
            mid = (left + right + 1)//2
            if target <= nums[mid]:
                left = mid
            else:
                right = mid - 1
        return left


s = Solution()

a = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3],
]
print(s.countNegatives(a))
