"""
    1st: brute force to compare every charactor with a hashtable

    Time    O(MN)
    Space   O(N)
    8 ms, faster than 100.00%
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        mapping = {}
        for i in range(len(order)):
            key = order[i]
            mapping[key] = i
        for i in range(1, len(words)):
            prev = words[i-1]
            cur = words[i]
            n = min(len(prev), len(cur))
            isOrdered = False
            for j in range(n):
                p = prev[j]
                c = cur[j]
                if mapping[p] < mapping[c]:
                    isOrdered = True
                    break
                elif mapping[p] > mapping[c]:
                    return False
                # else:
                #     continue
            if isOrdered:
                continue
            if prev[:n] == cur[:n] and len(prev) > len(cur):
                return False
        return True
