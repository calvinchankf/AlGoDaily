"""
    1st: prefix sum + 2 arrays
    - similar to lc915

    Time    O(N)
    Space   O(N)
    1716 ms
"""


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        forwardEvens = n * [0]
        forwardOdds = n * [0]
        backwardEvens = n * [0]
        backwardOdds = n * [0]

        pfsE = 0
        pfsO = 0
        for i in range(n):
            if i % 2 == 0:
                pfsE += nums[i]
            else:
                pfsO += nums[i]
            forwardEvens[i] = pfsE
            forwardOdds[i] = pfsO

        sfsE = 0
        sfsO = 0
        for i in range(n-1, -1, -1):
            if i % 2 == 0:
                sfsE += nums[i]
            else:
                sfsO += nums[i]
            backwardEvens[i] = sfsE
            backwardOdds[i] = sfsO

        res = 0
        for i in range(n):
            a, b, c, d = 0, 0, 0, 0
            if i-1 >= 0:
                a = forwardEvens[i-1]
                b = forwardOdds[i-1]
            if i+1 < n:
                c = backwardOdds[i+1]
                d = backwardEvens[i+1]
            evens = a + c
            odds = b + d
            if evens == odds:
                res += 1
        return res
