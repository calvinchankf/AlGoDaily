"""
    1st: queue

    Time    O(N)
    Space   O(N)
    48 ms, faster than 100.00%
"""


class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabets = []
        nums = []
        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                alphabets.append(c)
        if abs(len(alphabets) - len(nums)) > 1:
            return ''
        res = ''
        while len(alphabets) > 0 and len(nums) > 0:
            res += alphabets.pop()
            res += nums.pop()
        if len(alphabets) > 0:
            res += alphabets.pop()
        if len(nums) > 0:
            res = nums.pop() + res
        return res
