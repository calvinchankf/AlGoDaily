from typing import List

"""
    1st: dynamic programming, recursion + hashtable
    - similar to lc813
    - solve it by solving its subproblems, optimize the speed by caching the result of subproblems

    For example [1,15,7,9,2,5,10], 
    a subproblem can be [15,7,9,2,5,10] or [7,9,2,5,10] or [9,2,5,10]
    
    Time    O(K * N^2)
    Space   O(N)
    1684 ms, faster than 17.51% 
"""


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        return self.dfs(A, K, {})

    def dfs(self, nums, K, ht):
        if len(nums) == 0:
            return 0
        N = len(nums)
        key = (N, K)
        if key in ht:
            return ht[key]
        res = 0
        curMax = 0
        for i in range(min(N, K)):
            curMax = max(curMax, nums[i])
            temp = self.dfs(nums[i+1:], K, ht) + curMax * (i+1)
            res = max(res, temp)
        ht[key] = res
        return res


s = Solution()

a = [1, 15, 7, 9, 2, 5, 10]
b = 3
print(s.maxSumAfterPartitioning(a, b))

a = [20779, 436849, 274670, 543359, 569973, 280711, 252931, 424084, 361618, 430777, 136519, 749292, 933277, 477067, 502755, 695743, 413274, 168693, 368216, 677201, 198089, 927218,
     633399, 427645, 317246, 403380, 908594, 854847, 157024, 719715, 336407, 933488, 599856, 948361, 765131, 335089, 522119, 403981, 866323, 519161, 109154, 349141, 764950, 558613, 692211]
b = 26
print(s.maxSumAfterPartitioning(a, b))
