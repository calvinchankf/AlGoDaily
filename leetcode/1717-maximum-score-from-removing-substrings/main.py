"""
    1st: stacks
    - if x > y: remove all the AB first, then remove BA
    - else: remove BA, then remove AB

    Time    O(N)
    Space   O(N)
    632 ms, faster than 61.86%
"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        q = [c for c in s]
        if x > y:
            q, a = self.removeAB(q, x)
            q, b = self.removeBA(q, y)
            return a + b
        q, a = self.removeBA(q, y)
        q, b = self.removeAB(q, x)
        return a + b

    def removeAB(self, seq, x):
        res = 0
        q = []
        for c in seq:
            if len(q) > 0 and q[-1] == 'a' and c == 'b':
                q.pop()
                res += x
            else:
                q.append(c)
        return q, res

    def removeBA(self, seq, y):
        res = 0
        q = []
        for c in seq:
            if len(q) > 0 and q[-1] == 'b' and c == 'a':
                q.pop()
                res += y
            else:
                q.append(c)
        return q, res
