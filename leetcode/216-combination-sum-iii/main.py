"""
    1st: recursion
    - similar to lc77(combinations)

    Time    O(nCk)
    Space   O(nCk)
    80 ms, faster than 32.73% 
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i+1 for i in range(9)]
        self.res = []
        self.dfs([], nums, k, n)
        return self.res

    def dfs(self, chosen, nums, k, n):
        if len(chosen) == k:
            if n == 0:
                self.res.append(chosen)
            return
        for i in range(len(nums)):
            x = nums[i]
            self.dfs(chosen + [x], nums[i+1:], k, n-x)
