"""
    1st: hashtable
    - just save the graph in hashtable

    Time    O(N)
    Space   O(N)
    52 ms, faster than 87.49%
"""


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ht = {}
        for a, b in paths:
            if a not in ht:
                ht[a] = [b]
            else:
                ht[a].append(b)
            if b not in ht:
                ht[b] = []

        for key in ht:
            if len(ht[key]) == 0:
                return key


"""
    2nd: hashtable
    - same method as 1st approach but save the count

    Time    O(N)
    Space   O(N)
    48 ms, faster than 95.98%
"""


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ht = {}
        for a, b in paths:
            if a not in ht:
                ht[a] = 1
            else:
                ht[a] += 1
            if b not in ht:
                ht[b] = 0

        for key in ht:
            if ht[key] == 0:
                return key
