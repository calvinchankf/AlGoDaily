from collections import *

"""
    1st: hashtable
    - count the UAM(user active minutes) with a hashtable

    Time    O(N)
    Space   O(N)
    992 ms, faster than 89.96%
"""


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ht = defaultdict(set)
        for u, t in logs:
            ht[u].add(t)
        freqs = (k+1) * [0]
        for u in ht:
            f = len(ht[u])
            freqs[f] += 1
        freqs = freqs[1:]
        return freqs
