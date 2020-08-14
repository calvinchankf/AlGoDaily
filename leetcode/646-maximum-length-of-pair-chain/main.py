import sys
from typing import List
from functools import cmp_to_key

"""
    1st: sort the end times

    Time    O(NlogN)
    Space   O(N)
    244 ms, faster than 71.53%
"""


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = -sys.maxsize, 0

        def compare(a, b):
            return a[1] - b[1]

        arr = sorted(pairs, key=cmp_to_key(compare))
        for x, y in arr:
            if cur < x:
                cur = y
                res += 1
        return res


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
