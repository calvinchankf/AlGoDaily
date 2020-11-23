from collections import *

"""
    1st: dynamic programming, hashtable
    - learned from others
    - longest increasing subsequnce but 2D because we want to store the diff between any arr[i] and arr[j]
    - similar to lc1027, 1218

    for each index, store a hashtable of diff : count of longest subsequence
    
    e.g. [20,1,15,3,10,5,8]

    id| num | hashtable
    0 | 20:  { } becomes { -5: 1}
    1 | 1:  { -19: 1 }
    2 | 15: { -5: 1, 14: 1 }
              ^^^^^
    Stop at here, we see that 20 is in fact in our dp, and dp[0][-5] doesnt exist, so we should add ht[-5] = 1 to dp[0]
    Then it becomes...
    2 | 15: { -5: 2, 14: 1 }
              ^^^^^
    3 | 3:  { -17: 1, 2: 1, -12: 1}
    4 | 10: { -10: 1, 9: 1, -5: 1.......again
                            ^^^^^
    Stop at here, we see that 15 is in fact in our dp, and dp[2][-5] also exists, so we can add dp[2][-5] to dp[4][-5]. 
    Then it becomes...
    4 | 10: { -10: 1, 9: 1, -5: 3, 7:1 }
                            ^^^^^
    5 | 5: { -15: 1, 4: 1, -10: 1, 2: 1, -5: 1.....again
    Stop at here, we see that 15 is in fact in our dp, and dp[4][-5] also exists, so we can add dp[4][-5] to dp[5][-5]. 
    Then it becomes...
    5 | 5: { -15: 1, 4: 1, -10: 1, 2: 1, -5: 4 }

    ref:
    - https://leetcode.com/problems/longest-arithmetic-subsequence/discuss/274584/Same-as-LIS-problem-python-solution

    Time    O(N^2)
    Space   O(N)
    7088 ms, faster than 5.00% ???
"""


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        """
            dp = [{
                diff1: count1
            }, {
                diff1: count2
            },...]
        """
        dp = []
        for i in range(n):
            dp.append(Counter())
        res = 0
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in dp[j]:
                    dp[j][diff] = 1
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                res = max(res, dp[i][diff])
        return res


"""
    or we dont use counter
"""


class Solution(object):
    def longestArithSeqLength(self, A):
        n = len(A)
        ht = {}
        for i in range(n):
            ht[i] = {}
        res = 0
        for i in range(n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff not in ht[j]:
                    ht[j][diff] = 1
                if diff not in ht[i]:
                    ht[i][diff] = 0
                ht[i][diff] = max(ht[i][diff], ht[j][diff] + 1)
                res = max(res, ht[i][diff])
        return res
