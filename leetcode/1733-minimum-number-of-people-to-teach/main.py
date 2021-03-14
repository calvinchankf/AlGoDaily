
from collections import *

"""
    1st: brute force hashtable
    - for each language, count the number of people need to learn
    - the language with minimum people learn is the result

    Time    O(NM)
    Space   O(N)
    8356 ms, faster than 100.00% 
"""


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cache = defaultdict(set)
        for i in range(len(languages)):
            cache[i] = set(languages[i])

        res = 2**32
        for k in range(1, n+1):
            toTeach = set()
            for u, v in friendships:
                intersections = cache[u-1] & cache[v-1]
                if len(intersections) > 0:
                    continue
                if k not in cache[u-1]:
                    toTeach.add(u)
                if k not in cache[v-1]:
                    toTeach.add(v)
            res = min(res, len(toTeach))
        return res
