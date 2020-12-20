"""
    1st:
    - to avoid using sort, merge 2 arrays by putting the smaller item in iteratively

    Time    O(N)
    Space   O(N)
    204 ms, faster than 23.87%
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negs = []
        poss = []
        for x in A:
            if x < 0:
                negs.append(x**2)
            else:
                poss.append(x**2)
        negs.reverse()
        i, j = 0, 0
        res = []
        while i < len(negs) and j < len(poss):
            if negs[i] < poss[j]:
                res.append(negs[i])
                i += 1
            else:
                res.append(poss[j])
                j += 1
        if i < len(negs):
            res += negs[i:]
        if j < len(poss):
            res += poss[j:]
        return res
