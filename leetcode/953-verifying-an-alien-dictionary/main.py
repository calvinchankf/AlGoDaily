"""
    1st: brute force to compare every charactor with a hashtable

    Time    O(MN)
    Space   O(N)
    8 ms, faster than 100.00%
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
            key = order[i]
            mapping[key] = i

        for i in range(1, len(words)):
            prev = words[i-1]
            cur = words[i]
            n = min(len(prev), len(cur))
            curLargerThanPrev = False
            for j in range(n):
                p = prev[j]
                c = cur[j]
                if mapping[p] < mapping[c]:
                    curLargerThanPrev = True
                    break
                elif mapping[p] > mapping[c]:
                    return False
                else:
                    continue
            if curLargerThanPrev:
                continue
            if prev[:n] == cur[:n] and len(prev) > len(cur):
                return False
        return True
