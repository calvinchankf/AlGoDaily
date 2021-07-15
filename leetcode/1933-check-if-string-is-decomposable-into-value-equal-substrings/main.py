from collections import *

"""
    1st: string + hashtbale
    - split the string into substrings and check their lengths

    Time    O(N)
    Space   O(N)
    44 ms, faster than 100.00%
"""


class Solution:
    def isDecomposable(self, s: str) -> bool:
        lengths = Counter()
        sub = ''
        for i in range(len(s)):
            c = s[i]
            if len(sub) > 0:
                if c == sub[-1]:
                    if len(sub) == 3:
                        lengths[len(sub)] += 1
                        sub = c
                    else:
                        sub += c
                else:
                    lengths[len(sub)] += 1
                    sub = c
            else:
                sub += c
        lengths[len(sub)] += 1
        if len(lengths) == 1 and lengths[2] == 1:
            return True
        if len(lengths) == 2 and lengths[2] == 1 and 3 in lengths:
            return True
        return False
