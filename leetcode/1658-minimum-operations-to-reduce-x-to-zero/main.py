"""
    1st: prefix sum + binary search

    let's say with the example
    [1,1,4,2,3]
    [1,2,6,8,11] <- prefix sum A
    [11,10,9,5,3] <- suffix sum B (we can reverse it for binary search, easier to implement)
    Since the the question said that there are no negative numbers, the prefix&suffix sums must be sorted ascendingly.

    Now, want to do here is to find out the the point A[i] + B[j] == X, with minimum i+j
    One implementation detail is that, it is possible that we only need A[i] or B[i], so I simply add a zero to each of the arrays then do binary search.
    
    Time    O(NlogN)
    Space   O(N)
    3040 ms, faster than 5.05%
"""


class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        forwards = n * [0]
        pfs = 0
        for i in range(n):
            pfs += nums[i]
            forwards[i] = pfs
        sfs = 0
        backwards = n * [0]
        for i in range(n-1, -1, -1):
            sfs += nums[i]
            backwards[i] = sfs
        backwards.reverse()

        res = 2**32
        forwards.insert(0, 0)
        backwards.insert(0, 0)
        for i in range(n+1):
            a = forwards[i]
            j = self.bsearch(backwards, x - a)
            if j != -1 and i + j <= n:
                res = min(res, i + j)
        if res == 2**32:
            return - 1
        return res

    def bsearch(self, nums, target):
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
        return -1
