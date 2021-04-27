"""
    1st approach: counting

    e.g. 000111100
    
    0123456789AB <- index
    ------------
    000111100111
      ^   ^ ^  ^
      3   4
            2  3
    when we reach to index7, we add min(3, 4) to the result, and reset zeroCount = 0
    when we reach to index9, we add min(2, 4) to the result, add reset oneCount = 0
    when we reach to the end, we add min(2, 3) to the reuslt
    
    Time    O(n)
    Space   O(1)
    340 ms, faster than 12.29%
"""


class Solution(object):
    def countBinarySubstrings(self, s):
        res = 0
        zeros, ones = 0, 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i-1]:
                res += min(zeros, ones)
                if s[i] == '0':
                    zeros = 0
                else:
                    ones = 0
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
        res += min(zeros, ones)
        return res
