import sys
from typing import List

"""
    1st: recursion + hashtable
    - similar to lc410, lc1043
    - consider m = 2, we find out the Largest Sum of Averages in 2 loops, right?
    - so, when m = 3, we can reuse the result from m = 2
    - so, when m = 4, we can reuse the result from m = 3
    - ...and so on

    Time    O(M * N^2)
    Space   O(N)
    560 ms, faster than 31.13%
"""


class Solution(object):
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        self.ht = {}
        return self.dfs(A, K)

    def dfs(self, nums, m):

        n = len(nums)

        if m <= 0:
            return 0
        elif m == 1:
            total = sum(nums)
            return total / n

        key = (n, m)
        if key in self.ht:
            return self.ht[key]

        res = 0
        pfs = 0
        for i in range(n-1):
            pfs += nums[i]
            temp = self.dfs(nums[i+1:], m-1)
            n = i + 1
            res = max(res, temp + pfs / n)

        self.ht[key] = res
        return res


s = Solution()
a = [9, 1, 2, 3, 9]
b = 3
print(s.largestSumOfAverages(a, b))

a = [4663, 3020, 7789, 1627, 9668, 1356, 4207, 1133, 8765, 4649, 205, 6455, 8864, 3554, 3916, 5925, 3995, 4540, 3487, 5444, 8259, 8802, 6777, 7306,
     989, 4958, 2921, 8155, 4922, 2469, 6923, 776, 9777, 1796, 708, 786, 3158, 7369, 8715, 2136, 2510, 3739, 6411, 7996, 6211, 8282, 4805, 236, 1489, 7698]
b = 27
print(s.largestSumOfAverages(a, b))
