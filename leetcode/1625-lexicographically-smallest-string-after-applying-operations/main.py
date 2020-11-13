"""
    1st: DFS

    Time    O(100 N) for every number, there are 10 possibilities for each operation
    Space   O(100 N)
    2128 ms, faster than 64.63%
"""
class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        self.res = s
        seen = set()
        self.dfs(s, a, b, seen)
        return self.res
        
    def dfs(self, s, a, b, seen):
        if s in seen:
            return
        seen.add(s)
        if s < self.res:
            self.res = s
        
        # opA
        _s = ''
        for i in range(len(s)):
            if i%2 == 1:
                _s += str((int(s[i]) + a) % 10)
            else:
                _s += s[i]
        self.dfs(_s, a, b, seen)
        
        # opB
        n = len(s)
        self.dfs(s[n-b:] + s[:n-b], a, b, seen)