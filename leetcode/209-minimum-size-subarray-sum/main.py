from bisect import *
import sys


"""
    sliding window(2 pointers)
	- similar to lc3, 76
	- fast pointer to find the next item which sum up > target
	- once each the target, move the slow pointer to the right to see if the sum persist if sum = sum - nums[slow]

	Time	O(2n)
	Space 	O(1)
	60 ms, faster than 99.78%
	23jan2019
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        res = 2**32
        cur = 0
        j = 0
        for i in range(len(nums)):
            cur += nums[i]
            while cur >= target:
                res = min(res, i - j + 1)
                cur -= nums[j]
                j += 1
        if res == 2**32:
            return 0
        return res


"""
    2nd: upper bound binary search
    
    Time    O(NlogN)
    Space   O(N)
    80 ms, faster than 40.12%
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        pfss = n * [0]
        pfs = 0
        for i in range(n):
            pfs += nums[i]
            pfss[i] = pfs
        res = 2**32
        for i in range(n):
            j = bisect_right(pfss, pfss[i] - target)
            if j-1 >= 0 and pfss[i] - pfss[j-1] >= target:
                res = min(res, i - j + 1)
            elif pfss[i] >= target:
                res = min(res, i + 1)
        if res == 2**32:
            return 0
        return res
