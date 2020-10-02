
"""
    1st: 3 pointers
    - this is a sub-optimal approach, i use extra spaces to store the first m items from nums1
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        extra = nums1[:m]
        i, j, k = 0, 0, 0
        while i < m and j < n:
            if extra[i] < nums2[j]:
                nums1[k] = extra[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            nums1[k] = extra[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1
