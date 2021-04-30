"""
    1st: sort + hashtable
    - the score are unique, so we can just use the scores as keys in the hashtable

    Time    O(NlogN + N)
    Space   O(N)
    72 ms, faster than 57.60%
"""


class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        pairs = scores[:]
        pairs.sort(key=lambda x: -x)
        mapping = {}
        for i in range(len(pairs)):
            s = pairs[i]
            mapping[s] = i + 1
        res = []
        for s in scores:
            rank = mapping[s]
            if rank == 1:
                res.append("Gold Medal")
            elif rank == 2:
                res.append("Silver Medal")
            elif rank == 3:
                res.append("Bronze Medal")
            else:
                res.append(str(rank))
        return res
