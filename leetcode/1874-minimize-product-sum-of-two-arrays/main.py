"""
    1st: sort
    - sort the first array
    - reverse-sort the second array
    - the result is the product of nums1[i] and nums2[i]

    Time    O(NlogN)
    Space   O(1)
    1144 ms, faster than 100.00%
"""


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1.sort()
        nums2.sort(key=lambda x: -x)
        res = 0
        for i in range(n):
            res += nums1[i] * nums2[i]
        return res
