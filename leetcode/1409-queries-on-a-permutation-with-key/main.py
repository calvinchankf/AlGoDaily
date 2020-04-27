"""
    1st: binary search + brute force search

    Time    O(NlogN -> NN)
    Space   O(N)
    88 ms, faster than 55.20% 
"""


class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        nums = [i + 1 for i in range(m)]
        res = []
        for i in range(len(queries)):
            q = queries[i]
            start = len(res)
            idx = self.bsearch(nums, start, q)
            if idx == -1:
                idx = self.linearSearch(nums, start, q)
            res.append(idx)
            nums = [nums[idx]] + nums[:idx] + nums[idx+1:]
        return res

    def bsearch(self, nums, start, target):
        left = start
        right = len(nums)-1
        while left <= right:
            mid = (left + right)/2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1

    def linearSearch(self, nums, end, target):
        for i in range(end):
            if nums[i] == target:
                return i
