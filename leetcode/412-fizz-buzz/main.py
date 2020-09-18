"""
    1st approach: math

    Time    O(n)
    Space   O(n)
    48 ms, faster than 23.34%
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n+1):
            s = ''
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            if len(s) == 0:
                s = str(i)
            res.append(s)
        return res
