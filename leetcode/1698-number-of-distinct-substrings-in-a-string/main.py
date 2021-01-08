"""
    brute force

    Time    O(N^2)
    Space   O(N^2)
    992 ms, faster than 100.00% 
"""


class Solution:
    def countDistinct(self, s: str) -> int:
        hs = set()
        for i in range(len(s)):
            sub = ''
            for j in range(i, len(s)):
                sub += s[j]
                hs.add(sub)
        return len(hs)
