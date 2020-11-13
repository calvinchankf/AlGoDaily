"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    1656 ms, faster than 91.45%
"""


class SparseVector:
    def __init__(self, nums: List[int]):
        ht = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                ht[i] = nums[i]
        self.ht = ht

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in self.ht:
            if i in vec.ht:
                res += self.ht[i] * vec.ht[i]
        return res
