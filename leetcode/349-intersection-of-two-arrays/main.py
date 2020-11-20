"""
    1st approach: hashtable

    Time    O(A+B)
    Space   O(A+B)
    36 ms, faster than 97.24%
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ht = {}
        for x in nums1:
            ht[x] = True
        res = []
        for x in nums2:
            if x in ht:
                res.append(x)
                del ht[x]
        return res
