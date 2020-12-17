from collections import *

"""
    - very similar to 2sum

    Time    O(N)
    Space   O(N)
    700 ms, faster than 54.12% 
"""


class Solution(object):
    def maxOperations(self, nums, k):
        ops = 0
        counter = Counter()
        for x in nums:
            remain = k - x
            if remain in counter and counter[remain] > 0:
                counter[remain] -= 1
                ops += 1
            else:
                counter[x] += 1
        return ops
