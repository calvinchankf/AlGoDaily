"""
    1st: lower bound binary search
    - to deal with reversed order easier, use negative

    Time    O(BlogA)
    Space   O(1)
    2124 ms, faster than 12.46%
"""


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = [-x for x in nums1]
        nums2 = [-x for x in nums2]
        maxDiff = 0
        for j in range(len(nums2)):
            i = self.lowerBsearch(nums1, nums2[j], j)
            if 0 <= i < min(j, len(nums1)) and abs(nums1[i]) <= abs(nums2[j]):
                maxDiff = max(maxDiff, j - i)
        return maxDiff

    def lowerBsearch(self, nums, target, j):
        left = 0
        right = min(j, len(nums))
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


"""
    2nd: 2 pointers
    - for every number in A, we advance B
    - since A & B are sorted, we dont need to go back in B. So we can just use 2 pointers

    Time    O(A+B)
    Space   O(1)
    1008 ms, faster than 67.91%
"""


class Solution(object):
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        res = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                res = max(res, j - i)
                j += 1
        return res
