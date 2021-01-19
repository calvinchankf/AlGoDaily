"""
    1st approach: string

    TIme    O(logn)
    Space   O(logn)
    16 ms, faster than 92.79%
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        s = str(x)
        rev = s[::-1]
        temp = int(rev) * sign
        if temp < -2**31 or temp > 2**31-1:
            return 0
        return temp


"""
    2nd approach: math

    Time    O(logn)
    Space   O(1)
    24 ms, faster than 62.04%
"""


class Solution(object):
    def reverse(self, x):
        # +/-
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        # reverse numbers
        rev = 0
        while x > 0:
            rev = rev*10 + x % 10
            x //= 10
        # boundaries
        temp = int(rev) * sign
        if temp < -2**31 or temp > 2**31-1:
            return 0
        return temp
