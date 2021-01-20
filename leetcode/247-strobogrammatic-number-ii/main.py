"""
    1st: recursion
    - candidates are 0 1 6 8 9
    - for even numbers, we do recursion starting from ''
    - for even numbers, we do recursion starting from '0', '1', '8'

    Time    O(5^N)
    Space   O(5^N)
    144 ms, faster than 23.91% 
"""


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        m = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6'
        }
        self.res = []
        if n % 2 == 0:
            self.dfs(n//2, '', '', '', m)
        else:
            self.dfs(n//2, '', '0', '', m)
            self.dfs(n//2, '', '1', '', m)
            self.dfs(n//2, '', '8', '', m)
        return self.res

    def dfs(self, k, left, mid, right, m):
        if k == 0:
            s = left + mid + right
            if len(s) > 0 and str(int(s)) == s:
                self.res.append(s)
            return
        for c in m:
            self.dfs(k-1, left + c, mid, m[c] + right, m)
