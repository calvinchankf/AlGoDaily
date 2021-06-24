"""
    1st: binary search
    - mind the upper bound, need to +1 because it is possible that we can use up all the removables

    Time    O( min(S,P) * logR )
    Space   O(1)
    3932 ms, faster than 33.33%
"""


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left = 0
        right = len(removable) + 1
        while left < right:
            mid = (left + right) // 2
            _removable = set(removable[:mid])
            b = self.isSub(s, p, _removable)
            if b:
                left = mid + 1
            else:
                right = mid
        return left - 1

    def isSub(self, S, P, _removable):
        i, j = 0, 0
        while i < len(S) and j < len(P):
            if i in _removable:
                i += 1
                continue
            if S[i] == P[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(P)
