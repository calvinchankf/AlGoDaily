"""
    1st approach: hashtable

    Time    O(A+B)
    Space   O(A+B)
    32 ms, faster than 77.47%
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ht = Counter(nums1)
        res = []
        for x in nums2:
            if x in ht:
                res.append(x)
                ht[x] -= 1
                if ht[x] == 0:
                    del ht[x]
        return res
