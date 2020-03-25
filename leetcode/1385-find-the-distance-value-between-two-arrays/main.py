"""
    1st: sort + binary search

    Time    O(2NlogN)
    Space   O(1)
    92 ms, faster than 82.51%
"""


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for num in arr1:
            idx = self.bSearchNearest(arr2, num)
            diff = abs(num - arr2[idx])
            if diff > d:
                res += 1
        return res

    def bSearchNearest(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # checking
        if right < 0:
            return 0
        if left > len(nums)-1:
            return len(nums)-1
        # compare
        if abs(target-nums[right]) < abs(target-nums[left]):
            return right
        return left
