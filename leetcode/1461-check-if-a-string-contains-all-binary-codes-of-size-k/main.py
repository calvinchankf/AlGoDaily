"""
    1st: sliding window + hashtable
    - check all sub-strings of length k
    - the number of distinct sub-strings should be exactly 2^k

    Time    O(N)
    Space   O(N)
    432 ms, faster than 100.00%
"""


class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        hs = set()
        for i in range(len(s)-k+1):
            sub = s[i:i+k]
            hs.add(sub)
        return len(hs) == 2**k
