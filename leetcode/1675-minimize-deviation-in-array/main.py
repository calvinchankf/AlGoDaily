"""
    1st: sort + binary search

    Time    O(logN + N^2) insert takes O(N). This is slow but idk why it still passed OJ
    Space   O(N)
    3648 ms
"""


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums.sort()
        res = 2**32
        while nums[0] % 2 == 1:
            res = min(res, nums[-1] - nums[0])
            x = nums.pop(0) * 2
            j = self.upperBsearch(nums, x)
            nums.insert(j, x)
        while nums[-1] % 2 == 0:
            res = min(res, nums[-1] - nums[0])
            x = nums.pop() // 2
            j = self.upperBsearch(nums, x)
            nums.insert(j, x)
        return min(res, nums[-1] - nums[0])

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
