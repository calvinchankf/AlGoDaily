"""
    1st: string

    Time    O(N)
    Space   O(N)
    28 ms, faster than 100.00%
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        n = len(s1)
        diffA = set()
        diffB = set()
        for i in range(n):
            if s1[i] != s2[i]:
                if len(diffA) == 2:
                    return False
                diffA.add(s1[i])
                diffB.add(s2[i])
        return diffA == diffB
