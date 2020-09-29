"""
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    180 ms, faster than 59.58%
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hs = set()
        dup = -1
        for num in nums:
            if num in hs:
                dup = num
            else:
                hs.add(num)
        missing = -1
        for i in range(1, len(nums)+1):
            if i not in hs:
                missing = i
        return [dup, missing]


"""
    2nd approach: math

    originally, 	        abcdef=720
	now, 				    abcdcf=540

	and 					a+b+c+d+e+f=21
	now 					a+b+c+d+c+f=20
	
    so...
	e/c = 720/540 = 4/3
	e-c = 1
	
    solve the equation
	c = 3, e = 4

    However, when N=10000000, x! will stackoverflow the int32
	therefore we should not use 'mutiply'
    
    lets say for [1, 2, 3, 3, 5, 6] what if we...
	a^2 + b^2 + c^2 + d^2 + e^2 + f^2 = 91
    a^2 + b^2 + c^2 + c^2 + d^2 + f^2 = 84
    --------------------------------------
                            e^2 - c^2 = 7

	e - c = 1
	e + c = 7
	c=3, e=4

    Time    O(n)
    Space   O(n)
    180 ms, faster than 59.58%
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p1 = 0
        p2 = 0
        s1 = 0
        s2 = 0
        for i in range(1, len(nums)+1):
            p1 += i*i
            s1 += i
        for i in range(len(nums)):
            p2 += nums[i] * nums[i]
            s2 += nums[i]
        p_diff = p1 - p2
        s_diff = s1 - s2
        dup = (p_diff/s_diff - s_diff)/2
        missing = s_diff + dup
        return [dup, missing]
