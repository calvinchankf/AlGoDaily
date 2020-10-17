"""
    1st approach: recursion + hashtable
    - similar to classic coin change/knapsack problem
    - when we calculate recursively, there must be some redundant 'subtrees'. we can use a hashtable to avoid redundant calculation

    Time    O(DFT)
    Space   O(DF)
    748 ms, faster than 39.83%
"""


class Solution(object):
    def numRollsToTarget(self, d, f, target):
        total = self.dfs(target, d, f, {}})
        return total

    def dfs(self, d, f, target, ht):
        if target < 0:
            return 0
        if d == 0:
            if target == 0:
                return 1
            else:
                return 0
        key = (d, target)
        if key in ht:
            return ht[key]
        total = 0
        for i in range(1, f+1):
            total += self.dfs(d-1, f, target - i, ht)
        ht[key] = total % (10**9+7)
        return ht[key]
