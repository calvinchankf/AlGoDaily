"""
    1st: backtracking

    Time    O(2^N) for every digit, we either consider it in the current substring or the next substring
    Space   O(2^N)
    28 ms, faster than 98.19%
"""


class Solution:
    def splitString(self, s: str) -> bool:
        return self.backtrack(-1, -1, s)

    def backtrack(self, a, b, s):
        if len(s) == 0:
            return a != -1 and b != -1
        for i in range(1, len(s)+1):
            sub = s[:i]
            cur = int(sub)
            if b == -1 or b == cur + 1:
                if self.backtrack(b, cur, s[i:]):
                    return True
        return False
