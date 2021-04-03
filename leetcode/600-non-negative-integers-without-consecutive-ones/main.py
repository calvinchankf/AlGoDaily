"""
    1st: binary string contruction
    - it works in JS but fails in python

    Time    O(logN) -> O(N)
    Space   O(logN) -> O(N)
    LTE 180 / 527 test cases passed.
"""


class Solution(object):
    def findIntegers(self, num):
        if num < 1:
            return 0
        self.res = 1
        self.dfs(1, num)
        return self.res

    def dfs(self, cur, L):
        if cur > L:
            return
        self.res += 1
        if cur & 1 == 0:
            self.dfs(2 * cur + 0, L)
            self.dfs(2 * cur + 1, L)
        else:
            self.dfs(2 * cur + 0, L)
