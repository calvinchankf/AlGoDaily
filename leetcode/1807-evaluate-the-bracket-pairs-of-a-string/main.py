"""
    1st: hashtable

    Time    O(N)
    Space   O(N + M)
    932 ms, faster than 95.84%
"""


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        m = {}
        for a, b in knowledge:
            m[a] = b
        started = False
        cur = ''
        res = ''
        for c in s:
            if c == '(':
                started = True
            elif c == ')':
                if cur in m:
                    res += m[cur]
                else:
                    res += '?'
                started = False
                cur = ''
            elif started:
                cur += c
            else:
                res += c
        return res
