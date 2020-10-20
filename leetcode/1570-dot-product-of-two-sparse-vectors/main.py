"""
    Time    O(N)
    Space   O(N)
    1712 ms, faster than 100.00%
"""


class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        res = 0
        n = min(len(self.nums), len(vec.nums))
        for i in range(n):
            res += self.nums[i] * vec.nums[i]
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
