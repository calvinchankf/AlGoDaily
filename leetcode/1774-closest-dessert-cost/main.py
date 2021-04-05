"""
    1st: recursion
    
    Time    O(M3^N)
    Space   O(3^N)
    612 ms, faster than 50.00%
"""


class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        self.res = 2**32
        for bc in baseCosts:
            self.dfs(bc, toppingCosts, 0, target)
        return self.res

    def dfs(self, cur, toppingCosts, i, target):
        if abs(cur - target) < abs(self.res - target):
            self.res = cur
        elif abs(cur - target) == abs(self.res - target) and cur < self.res:
            self.res = cur

        if i < len(toppingCosts):
            self.dfs(cur, toppingCosts, i+1, target)
            self.dfs(cur + 1 * toppingCosts[i], toppingCosts, i+1, target)
            self.dfs(cur + 2 * toppingCosts[i], toppingCosts, i+1, target)
