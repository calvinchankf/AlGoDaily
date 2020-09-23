import sys


"""
    sliding window(2 pointers)
	- similar to lc3, 76
	- fast pointer to find the next item which sum up > target
	- once each the target, move the slow pointer to the right to see if the sum persist if sum = sum - nums[slow]

	Time	O(2n)
	Space 	O(1)
	8ms ms beats 100%
	23jan2019
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        res = sys.maxsize
        j = 0
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            while curSum >= s:
                if curSum >= s:
                    res = min(res, i - j + 1)
                curSum -= nums[j]
                j += 1
        if res == sys.maxsize:
            return 0
        return res
