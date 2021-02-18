"""
    1st: hashtable outdegree

    Time    O(N)
    Space   O(N)
    48 ms, faster than 95.98%
"""


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outdegrees = {}
        for a, b in paths:
            outdegrees[a] = 0
            outdegrees[b] = 0
        for a, b in paths:
            outdegrees[a] += 1
        for key in outdegrees:
            if outdegrees[key] == 0:
                return key
        return ''
