from collections import defaultdict

"""
    1st: array + math

    Time    O(N log N)
    Space   O(N)
    96 ms, faster than 78.82%
"""


from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        ht = defaultdict(int)
        largestCount = 0
        res = 0
        for i in range(1, n+1):
            key = self.getKey(i)
            ht[key] += 1
            if ht[key] > largestCount:
                largestCount = ht[key]
                res = 1
            elif ht[key] == largestCount:
                res += 1
        return res

    def getKey(self, x):
        res = 0
        while x > 0:
            res += x % 10
            x //= 10
        return res
