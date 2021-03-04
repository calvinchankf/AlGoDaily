"""
    1st: math

    Time    O(N)
    Space   O(1)
    48 ms, faster than 53.33%
"""


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        orig = [0, 0]
        dis = self.getDistance(orig, target)
        for g in ghosts:
            _dis = self.getDistance(g, target)
            if _dis <= dis:
                return False
        return True

    def getDistance(self, A, B):
        return abs(A[0] - B[0]) + abs(A[1] - B[1])
