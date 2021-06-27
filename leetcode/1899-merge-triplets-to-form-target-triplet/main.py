from collections import *

"""
    1st: hashtable
    - since we can swap any number of times, we just care about the triplets which a <= target[0] and b <= target[1] and c <= target[2]

    Time    O(N)
    Space   O(N)
    2060 ms, faster than 82.77% 
"""


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        _triplets = []
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                _triplets.append([a, b, c])
        first = Counter()
        second = Counter()
        third = Counter()
        for a, b, c in _triplets:
            first[a] += 1
            second[b] += 1
            third[c] += 1
        return target[0] in first and target[1] in second and target[2] in third
