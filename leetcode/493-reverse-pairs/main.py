"""
    1st: Binary Indexed Tree + binary search
    - similar to leetcode 1885

    let's say there is a distinct sorted nums, we use BIT to count the occurence of every number
    nums       [1, 3, 6, 8, 9]
    BIT     [0, 0, 0, 0, 0, 0]

    if we insert 6, increment the count of BIT[3] (because BIT[3] is the freq for '6')
    nums       [1, 3, 6, 8, 9]
    BIT     [0, 0, 0, 1, 0, 0]

    if we insert 9,
    nums       [1, 3, 6, 8, 9]
    BIT     [0, 0, 0, 1, 0, 1]

    if we insert 3,
    nums       [1, 3, 6, 8, 9]
    BIT     [0, 0, 1, 1, 0, 1]

    if we insert 6,
    nums       [1, 3, 6, 8, 9]
    BIT     [0, 0, 1, 2, 0, 1]

    if we insert 6,
    nums       [1, 3, 6, 8, 9]
    BIT     [0, 0, 1, 3, 0, 1]

    with BIT, we can calculate the range sum between any indices [i, j] in O(logN)

    Time    O(NlogN)
    Space   O(N)
    2872 ms, faster than 31.37%
"""


class BinaryIndexedTree(object):

    def __init__(self, n):
        self.fenwickTree = (n+1) * [0]

    def update(self, i, val):
        k = i + 1
        while k < len(self.fenwickTree):
            self.fenwickTree[k] += val
            k += k & -k

    def getSum(self, i):
        s = 0
        k = i + 1
        while k > 0:
            s += self.fenwickTree[k]
            k -= k & -k
        return s

    def getRangeSum(self, i, j):
        return self.getSum(j) - self.getSum(i-1)


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sortedDistincts = nums[:]
        sortedDistincts = list(set(sortedDistincts))
        sortedDistincts.sort()
        tree = BinaryIndexedTree(len(sortedDistincts))

        nn = len(nums)
        n = len(sortedDistincts)

        res = 0
        for i in range(nn):
            x = nums[i]

            j = self.upperBsearch(sortedDistincts, 2*x)
            if j < nn:
                res += tree.getRangeSum(j, n-1)

            j = self.lowerBsearch(sortedDistincts, x)
            if j < nn:
                tree.update(j, 1)
        return res

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right
