from collections import defaultdict
from typing import List

"""
    0th: longest increasing subsequnce
    
    Time    O(N^2)
    TLE
"""


class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        n = len(arr)
        dp = n * [1]
        for i in range(n):
            maxLen = 0
            for j in range(i):
                if arr[j] == arr[i] - difference:
                    maxLen = max(maxLen, dp[j])
            dp[i] += maxLen
        return max(dp)


"""
    1st: dyanamic programming with hashtable
    - similar to lc560 but witout prefix sum
    - related to lc1027
    - use a hashtable to store the { distinct number : max length of a sequence }

    e.g.
    [1, 5, 7, 8, 5, 3, 4, 2, 1], -2
     1  1  1  1  2  3  1  2  4       <- for each number, find if ht[x-dff] exists and update ht[x] with the max length of a sequence
    
    Time    O(N)
    Space   O(N)
    664 ms, faster than 26.39%
"""


class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        ht = Counter()
        for x in arr:
            remain = x - difference
            if remain in ht:
                ht[x] = max(ht[x], ht[remain] + 1)
            else:
                ht[x] = 1
        return max(ht.values())
