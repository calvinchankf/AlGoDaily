
from collections import Counter

"""
    hashtable + sort + greedy

    e.g.1. "aaaabbbbccccdddd"
    
    hashtable: {
        a: 4,
        b: 4,
        c: 4,
        d: 4
    }
    out goal is to make it {
        a: 4,
        b: 3, # 4-3 = 1
        c: 2, # 4-2 = 2
        d: 1, # 4-1 = 3
    }
    we can sort the freqs descendingly and decrement the freq for every character,
    the result will be the diffs

    mind the case that with only count = 1 for some characters
    e.g.2 "bbcebab"

    hashtable: {
        b: 4,
        c: 1,
        e: 1,
        a: 1
    }
    out goal is to make it {
        a: 4,
        b: 1,
        c: 0,
        d: 0,
    }

    Time    O(N + 26log26 + 26)
    Space   O(26)
    160 ms, faster than 33.33%
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        freqs = []
        for key in counter:
            freqs.append(counter[key])
        freqs.sort(reverse=True)
        seen = set()
        seen.add(freqs[0])
        res = 0
        for i in range(1, len(freqs)):
            if freqs[i] in seen:
                temp = freqs[i]
                freqs[i] = max(freqs[i-1] - 1, 0)
                res += temp - freqs[i]
            seen.add(freqs[i])
        return res
