from collections import defaultdict

"""
    1st: DFS

    ref:
    - https://leetcode.com/problems/optimal-account-balancing/discuss/95363/Easy-backtracking-+-greedy-solution-with-explanation-(Python-Accepted)/99779

    e.g. transactions = [
        [6, 0, 50],
        [1, 6, 40],
        [2, 6, 10],
        [6, 3, 40],
        [5, 6, 25],
        [6, 7, 10],
        [7, 1, 10],
        [8, 9, 9]
    ]
    
    1. balances for everyone = {
        0:50, 
        1:-30, 
        2:-10, 
        3:40, 
        4:10, 
        5:-25, 
        6:-35, 
        7:0,
        8: -9,
        9: 9
    }

    2. filter out the zeros. Since we only care about the count
    [50, -30, -10, 40, -25, -25, -9, 9]

    3. in each recursion, find the counteropart first and narrow down the range, so the e.g. becomes
    [50, -30, -10, 40, -25, -25]

    4.  - for every possible pair, sum them up
        - for all pairs, find the pair with minimal number of steps to reach the bottom
    
    [20, -10, 40, -25, -25] <- sum 50 and -30
    [-30, 40, 40, -25, -25] <- sum 50 and -10
    [-30, -10, 40, 25, -25] <- sum 50 and -25
    [-30, -10, 40, -25, 25] <- sum 50 and the last -25

    In the next recursion, do the same thing.
    Let's say we consider, [20, -10, 40, -25, -25]

    [10, 40, -25, -25] sum 20 and -10
    [-10, 40, -5, -25] sum 20 and -25
    [-10, 40, -25, -5] sum 20 and the last -25
    ...

    Time    O(N!) worst ??? 
                For the worst case: 
                every number has no counterpart, 
                there are n-1 possibilities to subtract(then to the next recursion)

    Space   O(N + H!) H: height of the recursion tree
    504 ms, faster than 62.86% 
"""


class Solution:
    def minTransfers(self, transactions):
        ht = defaultdict(int)
        for x, y, z in transactions:
            ht[x] -= z
            ht[y] += z
        # filter not all the zero balances
        balences = [ht[person] for person in ht if ht[person] != 0]

        return self.dfs(balences)

    def dfs(self, balences):
        # base case
        if len(balences) == 0:
            return 0
        # no operation is needed at index 0, consider the rest of the balences
        if balences[0] == 0:
            return self.dfs(balences[1:])
        # try to find the counterpart for balences[0]
        for i in range(1, len(balences)):
            if balences[0] == -balences[i]:
                clone = balences[1:i] + [0] + balences[i+1:]
                return 1 + self.dfs(clone)
        # for every possible pair, sum them up
        # for all pairs, find the pair with minimal number of steps to reach the bottom
        res = []
        for i in range(1, len(balences)):
            if balences[0] * balences[i] < 0:
                clone = balences[1:i] + \
                    [balences[i]+balences[0]] + \
                    balences[i+1:]
                steps = self.dfs(clone)
                res.append(steps)
        # we now merge balences[0] and balences[i], so increment the count
        return 1 + min(res)


s = Solution()

# 4
a = [
    [6, 0, 50],
    [1, 6, 40],
    [2, 6, 10],
    [6, 3, 40],
    [5, 6, 25],
    [6, 7, 10],
    [7, 1, 10]
]
print(s.minTransfers(a))
