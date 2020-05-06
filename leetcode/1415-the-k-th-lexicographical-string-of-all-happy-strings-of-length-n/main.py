"""
    1st: recursion
    - similar to generate subsets/combinations

    Time    O(3 * 2^n)
    Space   O(2^n)
    220 ms, faster than 100.00%
"""


class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.res = []
        self.dfs('', n)
        if k > len(self.res):
            return ''
        return self.res[k-1]

    def dfs(self, chosen, n):
        if len(chosen) == n:
            self.res.append(chosen)
            return
        for c in ['a', 'b', 'c']:
            if len(chosen) == 0 or c != chosen[-1]:
                self.dfs(chosen + c, n)
