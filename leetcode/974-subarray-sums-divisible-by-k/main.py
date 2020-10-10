"""
    1st approach: similar to zero sum subarray
    - if prefixSum[i]%K == prefixSum[j]%k, it means that A[i+1:j] is divisible by K

    ref:
    - https://leetcode.com/problems/subarray-sums-divisible-by-k/discuss/217979/Pictured-Explanation-Python-O(n)-Clean-Solution-8-Lines!

    Time    O(n)
    Space   O(n)
    268 ms, faster than 94.01%
"""


class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        result = 0
        pfs = 0
        ht = {}
        for i in range(len(A)):
            pfs += A[i]

            mod = pfs % K
            if mod == 0:
                result += 1

            if mod in ht:
                result += ht[mod]

            if mod in ht:
                ht[mod] += 1
            else:
                ht[mod] = 1
        return result
