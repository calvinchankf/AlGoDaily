"""
    1st approach: stack

    Time    O(n)
    Space   O(1)
    44 ms, faster than 86.88%
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        stack = []
        for c in s:
            val = ht[c]
            if len(stack) > 0 and stack[-1] < val:
                stack[-1] = val - stack[-1]
            else:
                stack.append(val)
        return sum(stack)


"""
    2nd approach:
    - compare with prev value and if prev value < cur value
        1. undo previous addition
        2. add m[cur] - m[prev]
    - if no smaller bigger values, just do addition

    Time    O(n)
    Space   O(1)
    52 ms, faster than 97.49%
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = m[s[0]]
        for i in range(1, len(s)):
            prev = s[i-1]
            cur = s[i]
            if m[prev] < m[cur]:
                res -= m[prev]
                res += m[cur] - m[prev]
            else:
                res += m[cur]
        return res
