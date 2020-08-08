"""
    1st approach: greedy?
    1. if A - B >= 2, add 2 a and 1 b
    2. else, add them one by one
    3. if B - A >=2, same logic with 1) and 2)
    4. the question mentioned that the input must be valid, so don't need specific checking

    Time    O(A+B)
    Space   O(A+B) the result string
    16 ms, faster than 98.48%
"""


class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A == B:
            return 'ab' * A
        res = ''
        if A > B:
            while A > 0 or B > 0:
                if A - B >= 2:
                    res += 'aa'
                    A -= 2
                    if B > 0:
                        res += 'b'
                        B -= 1
                else:
                    res += 'a'
                    A -= 1
                    if B > 0:
                        res += 'b'
                        B -= 1
        elif B > A:
            while A > 0 or B > 0:
                if B - A >= 2:
                    res += 'bb'
                    B -= 2
                    if A > 0:
                        res += 'a'
                        A -= 1
                else:
                    res += 'b'
                    B -= 1
                    if A > 0:
                        res += 'a'
                        A -= 1
        return res
