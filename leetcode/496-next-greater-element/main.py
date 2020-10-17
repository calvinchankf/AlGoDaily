"""
    2st approach: stack + hashtable
    - the stack only stores the smaller items n the top
    - so when we iterate through the nums, if current num > stack.top(), put the current num is the next greater number of stack.top()
    - do step 2 in a loop
    - after we have done step2,3, if we still have numbers in the stack, it means that they dont have the next greater number

    Time    O(2n + m) m:nums1, n:nums2
    Space   O(n)
    36 ms, faster than 72.26%
"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ht = {}
        stack = []
        for x in nums2:
            while len(stack) > 0 and stack[-1] < x:
                top = stack.pop()
                ht[top] = x
            stack.append(x)
        res = []
        for x in nums1:
            if x in ht:
                res.append(ht[x])
            else:
                res.append(-1)
        return res
