
from collections import *

"""
    1st: better brute force with hastable
    - for every index, go forward to see if we can slice the string with all the words
    - optimization:
        - hashtable for lookup
        - slice the substring with jumps (of length L, becos all the words have the same length)
        - only iterate the s to the point that the suffix substring has enough characters(LN)

    Time    O(NM) N=len(s), M=total num of characters in words
    Space   O(M)
    
    original:   5064ms, faster than 7.51%
    optimized:  480 ms, faster than 57.34% 
"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordFreqs = Counter(words)
        N = len(words)
        L = len(words[0])
        LN = L * N
        res = []
        for i in range(len(s)-LN+1):  # optimization
            curFreqs = Counter()
            for j in range(i, i+LN, L):  # optimization
                cur = s[j:j+L]
                if cur in wordFreqs:
                    curFreqs[cur] += 1
                    if curFreqs[cur] > wordFreqs[cur]:
                        break
                else:
                    break
            if wordFreqs == curFreqs:
                res.append(i)
        return res
