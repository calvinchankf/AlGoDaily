"""
    1st approach: recursion
    - similar to lc131, 132, 139, 140
    - when we do recursion to slice candidates, we can check there are any palindromes from start to i, s[:i+1]
    - if yes, we can do the next recusion starting from i+1

    e.g. abcdcbe

    when it comes to the first b, the palindromes from the b are
    b
    bcdcb

    when it comes to the c, the palindromes from the c are
    c
    cdc


    ref:
    - https://leetcode.com/problems/palindrome-partitioning/discuss/42100/Python-easy-to-understand-backtracking-solution.

    Time    O(n * 2^n) the worst case all characters are the same, so for each character we can split or contain
    Space   O(n) the depth of the recursion tree
    76 ms, faster than 83.58%
"""


class Solution(object):
    def partition(self, s):
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, cur):
        if len(s) == 0:
            self.res.append(cur)
            return
        for i in range(len(s)):
            sub = s[:i+1]
            if sub == sub[::-1]:
                self.dfs(s[i+1:], cur + [sub])


"""
    same logic but with optimization
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, chosen):
        if len(s) == 0:
            self.res.append(chosen)
        sub = ''
        revSub = ''
        for i in range(len(s)):
            sub += s[i]
            revSub = s[i] + revSub
            if sub == revSub:
                self.dfs(s[i+1:], chosen + [sub])
