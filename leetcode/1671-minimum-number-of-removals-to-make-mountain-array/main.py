"""
    1st: dynamic programming
    - similar to lc198, 300, 1671
    1. minimum delete to make an array increasing = longest increasing subsequence
    2. minimum delete to make a mountain array = longest increasing subsequence from the left + longest increasing subsequence from the right

    corner case: [9,8,1,7,6,5,4,3,2,1]
    [9,8,1,7,6,5,4,3,2,1]
         ^
         dont remove this. Becos this will make a decreasing array but not mountain
    [9,8,1,7,6,5,4,3,2,1]
     ^ ^
     we should remove these 2

    Time    O(2N^2)
    Space   O(2N)
    3492 ms, faster than 33.33%
"""


class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 1
        forward = n * [1]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    forward[i] = max(forward[i], forward[j] + 1)
        backward = n * [1]
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    backward[i] = max(backward[i], backward[j] + 1)
        res = n * [0]
        for i in range(1, n-1):
            res[i] = forward[i] + backward[i] - 1
        return n - max(res)
