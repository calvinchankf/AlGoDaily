"""
    1st: sort + binary search
    - for every number in nums2, find the nearest number from nums1

    Time    O(NlogN)
    Space   O(N)
    1324 ms, faster than 63.77%
"""


class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        n = len(nums1)
        sortedNums1 = sorted(nums1)

        totalDiff = 0
        for i in range(n):
            totalDiff += abs(nums1[i] - nums2[i])

        res = totalDiff
        for i in range(n):
            j = self.bSearchNearest(sortedNums1, nums2[i])
            diff = abs(nums1[i] - nums2[i])
            _diff = abs(sortedNums1[j] - nums2[i])
            res = min(res, totalDiff - diff + _diff)

        return res % (10**9+7)

    def bSearchNearest(self, nums, target):
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
        # bounds checking
        if right < 0:
            return 0
        if left > len(nums)-1:
            return len(nums)-1
        # compare
        if abs(target-nums[right]) < abs(target-nums[left]):
            return right
        return left
