"""
    1st: hashtable

    Time    O(NL) N: number of words, W: average length of every word
    Space   O(1)
    200 ms, faster than 100.00%
"""


class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0
        for w in words:
            ifContain = True
            for c in w:
                if c not in allowed:  # there are at most 26 characters, no need to use hastable
                    ifContain = False
            if ifContain:
                count += 1
        return count
