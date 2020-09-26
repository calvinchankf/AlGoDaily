import sys
from typing import List
from functools import cmp_to_key

"""
    1st: sort the end times
    - activity selection

    ref:
    - https://www.cse.cuhk.edu.hk/~taoyf/course/3160/19-fall/lec/disj_intv.pdf
    - https://en.wikipedia.org/wiki/Activity_selection_problem

    Time    O(NlogN)
    Space   O(N)
    244 ms, faster than 71.53%
"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        intvs = sorted(pairs, key=lambda x: x[1])
        count = 0
        pos = -sys.maxsize
        for s, e in intvs:
            if s > pos:
                pos = e
                count += 1
        return count


"""
    2nd: dynamic programming
    - similar to lc300

    Time    O(N^2)
    Space   O(N)
    2716 ms, faster than 32.43%
"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = n * [1]
        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
