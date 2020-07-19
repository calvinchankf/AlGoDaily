from typing import List
from math import log, ceil, floor

"""
    2nd: Binary Lifting, learned from others
    - dp[i][j] indicates the 2^j parent of i
    - dp[i][j] = dp[ dp[i][j-1] ][j-1]

    The reason is, lets say here we have a single child tree
    0 > 1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 > 9 > 10

    let f() = getKthAncestor()
    
    f(10, 5) can be
    = f(f(10, 1), 4) = f(9, 4) = 5
    = f(f(10, 2), 3) = f(8, 3) = .... = -1
    = f(f(10, 3), 2) = .... = -1
    = f(f(10, 4), 1) = f(6, 1) = 5
    = ...

    see ./idea.png for details

    ref:
    - https://www.youtube.com/watch?v=Vvk4xjLfk84
    - https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node/solution/li-kou-zai-zhu-jian-ba-acm-mo-ban-ti-ban-shang-lai/

    Time of init()              O(NlogN)
    Time of getKthAncestor()    O(logN)
    Space                       O(N)
    1232 ms, faster than 74.92% 
"""


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        max_pow = int(ceil(log(n, 2)))

        self.dp = [[-1] * (max_pow + 1) for i in range(n)]

        for i in range(len(parent)):
            self.dp[i][0] = parent[i]

        for i in range(n):
            for j in range(1, max_pow):
                if self.dp[i][j-1] == -1:
                    break
                self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        if k == 0:
            return node
        if node == 0 or node == -1:
            return -1
        power = int(floor(log(k, 2)))
        return self.getKthAncestor(self.dp[node][power], k - 2**power)
