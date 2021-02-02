"""
    1st: array
    - check against the prev word on every character

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


"""
    2nd: optimization of the 1st
    - move character check to above, for case ["apple","app"] <= False, such that we dont need a boolean
    
    Time    O(MN)
    Space   O(N)
    32 ms, faster than 85.11% 
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        m = {}
        for i in range(len(order)):
            c = order[i]
            m[c] = i
        for i in range(1, len(words)):
            prev = words[i-1]
            cur = words[i]
            n = min(len(prev), len(cur))
            if prev[:n] == cur[:n] and len(prev) > len(cur):
                return False
            # then we dont need to use a boolean
            for j in range(n):
                p = m[prev[j]]
                c = m[cur[j]]
                if p < c:
                    break
                elif p > c:
                    return False
        return True
