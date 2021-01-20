"""
    1st: recursion
    - lc543, lc414, lc1522

    Time    O(N)
    Space   O(H)
    84 ms, faster than 100.00%
"""


class Solution:
    def diameter(self, root: 'Node') -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node == None:
            return 0
        largest1 = 0
        largest2 = 0
        for child in node.children:
            d = self.dfs(child)
            if d > largest1:
                largest2 = largest1
                largest1 = d
            elif d > largest2:
                largest2 = d
        self.res = max(self.res, largest1 + largest2)
        return max(largest1, largest2) + 1
