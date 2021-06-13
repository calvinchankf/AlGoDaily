"""
    1st: hashtable + math
    - for every character, its frequency must be divisible by N

    Time    O(NW)
    Space   O(26)
    84 ms, faster than 50.00%
"""


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        N = len(words)
        ht = 26 * [0]
        for w in words:
            for c in w:
                i = ord(c) - ord('a')
                ht[i] += 1
        for i in ht:
            if i % N > 0:
                return False
        return True
