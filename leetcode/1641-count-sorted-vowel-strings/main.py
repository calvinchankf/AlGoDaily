"""
    1st: brute force recursion(combinations)
    - similar to lc77

    Time    O(nCr)
    Space   O(nCr)
    7156 ms, faster than 12.88%
"""
class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.dfs(n, 0)
        return self.res
    
    def dfs(self, n, k):
        if n == 0:
            self.res += 1
            return
        for i in range(k, 5):
            self.dfs(n-1, i)