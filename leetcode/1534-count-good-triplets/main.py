"""
    1st: brute force

    Time    O(N^3)
    Space   O(1)
    832 ms, faster than 100.00%
"""


class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ij = abs(arr[i] - arr[j])
                    jk = abs(arr[j] - arr[k])
                    ik = abs(arr[i] - arr[k])
                    if ij <= a and jk <= b and ik <= c:
                        res += 1
        return res
