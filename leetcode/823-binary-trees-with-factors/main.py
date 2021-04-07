
from collections import *

"""
    1st: dynamic programming
    - learned from others
    1. each integer A[i] = X will always have one tree with only itself
    2. if X has divisor Y in the map, and if X/Y also in the map
        then X can be the root of its left subtree, and X/Y can be the root of its right subtree;
        the number of such tree is cache[X] * cache[X/Y]
    3. sum the cache values
    ref:
    https://leetcode.com/problems/binary-trees-with-factors/discuss/126277/Concise-Java-solution-using-HashMap-with-detailed-explanation.-Easily-understand!!!
    Time    O(N^2)
    Space   O(N)
"""


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        cache = Counter()
        for i in range(len(arr)):
            x = arr[i]
            count = 1
            for y in cache:
                if x % y == 0 and x // y in cache:
                    count += cache[x//y] * cache[y]
            cache[x] = count
        res = 0
        for x in cache:
            res += cache[x]
            res %= 10**9 + 7
        return res
