from collections import *

"""
    1st approach
	- hashtable
	1. in each iteration, transform the string into a key(diff between characters)
	2. keep in mind that, az, ba are in the same group

	Time		O(n)
	Space		O(n)
	28 ms, faster than 97.91%
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for s in strings:
            diffs = []
            for i in range(1, len(s)):
                c = s[i]
                p = s[i-1]
                diff = (ord(c) - ord(p) + 26) % 26
                diffs.append(diff)
            key = tuple(diffs)
            ht[key].append(s)
        
        res = []
        for key in ht:
            res.append(ht[key])
        return res