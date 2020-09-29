"""
    1st: backtracking (using recursion + hashtable)
    - similar to lc139, 140, 472
    - use 2 hashtables to save the exact mapping of each of the pattern charactors : portion of string
    - use recursion to try all the possibilites when we slice the remaining pattern and the remaining string

    Look at the corner case:
    p = twt
    s = ttwtt
    Be careful that for the last p = "" and s = "t", we cannot just backtrack directly 
    because t:tt was also mapped earlier in the beginning
    Therefore, we need to check if a mapping was made earlier before we backtrack

    Time    O(?) <- it is hard to determine
    Space   O(P+S)
    472 ms, faster than 10.87% 
"""


class Solution(object):
    def wordPatternMatch(self, pattern, s):
        forward = {}
        backward = {}
        b = self.backtracking(pattern, s, forward, backward)
        return b

    def backtracking(self, pattern, s, forward, backward):
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) == 0 or len(pattern) == 0:
            return False

        p = pattern[0]
        for i in range(len(s)):
            cand = s[:i+1]

            if p in forward and forward[p] != cand:
                continue
            if cand in backward and backward[cand] != p:
                continue

            wasMapped = False
            if p not in forward and cand not in backward:
                forward[p] = cand
                backward[cand] = p
            else:
                wasMapped = True

            b = self.backtracking(pattern[1:], s[i+1:], forward, backward)
            if b:
                return True

            if not wasMapped:
                del forward[p]
                del backward[cand]

        return False
