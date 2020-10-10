"""
    3rd approach: learned from others
	- calculate the products from the front & from the back
		e.g.
								2			3 		4 		5
						->	1		1*2		2*3		2*3*4
							3*4*5	4*5		5*1			1		<-
							-----------------------
			result = 60		20		30			12
	- the cruz of the question is to learn this approach, it is slow but it doesn't matter
	Time	O(3n)
	Space	O(2n)
	104 ms, faster than 61.41%
	8ay2019
"""


class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        forward = n * [1]
        backward = n * [1]
        for i in range(1, n):
            forward[i] = forward[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            backward[i] = backward[i+1] * nums[i+1]
        res = n * [1]
        for i in range(n):
            res[i] = forward[i] * backward[i]
        return res
