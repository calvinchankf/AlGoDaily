"""
    1st approach: 2 pointers
	- each digit = byteA + byteB + carry
	- add the digits until no more carry, a, b

    Time    O(A+B + max(A, B))
    Space   O(A+B)
    32 ms, faster than 39.01%
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        res = ''
        while i >= 0 or j >= 0 or carry > 0:
            x = 0
            y = 0
            if i >= 0:
                x = int(a[i])
            if j >= 0:
                y = int(b[j])
            c = x + y + carry
            res = str(c % 2) + res
            carry = c // 2
            i -= 1
            j -= 1
        return res
