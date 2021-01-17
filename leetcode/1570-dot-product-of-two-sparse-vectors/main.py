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


"""
    2nd: 2 pointers

    Time    O(N)
    Space   O(N)
    1592 ms, faster than 28.73%
"""


class SparseVector:
    def __init__(self, nums):
        self.nonZeros = []
        for i in range(len(nums)):
            x = nums[i]
            if x != 0:
                self.nonZeros.append((i, x))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        i, j = 0, 0
        A = self.nonZeros
        B = vec.nonZeros
        res = 0
        while i < len(A) and j < len(B):
            if A[i][0] == B[j][0]:
                res += A[i][1] * B[j][1]
                i += 1
                j += 1
            elif A[i][0] < B[j][0]:
                i += 1
            else:
                j += 1
        return res
