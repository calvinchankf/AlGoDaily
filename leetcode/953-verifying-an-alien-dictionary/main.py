"""
    1st: brute force to compare every charactor with a hashtable

    Time    O(MN)
    Space   O(N)
    20 ms, faster than 90.49%
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        mapping = {}
        for i in range(len(order)):
            mapping[order[i]] = i

        for i in range(1, len(words)):
            prev = words[i-1]
            cur = words[i]
            n = min(len(prev), len(cur))
            for j in range(n):
                p = prev[j]
                c = cur[j]
                if mapping[p] < mapping[c]:
                    break
                elif mapping[p] > mapping[c]:
                    return False
            if prev[:n] == cur[:n] and len(prev) > len(cur):
                return False
        return True
