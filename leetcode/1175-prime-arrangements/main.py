"""
    1st: dynamic programming + math
    - use DP to find all the primes <= n
    - the result is numOfPrimes! * (n-numOfPrimes)!

    Time    O(N^2)
    Space   O(N)
    32 ms, faster than 8.79%
"""


class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        pCount = self.countPrimes(n)
        temp = self.factorial(pCount) * self.factorial(n-pCount)
        return temp % (10**9+7)

    def factorial(self, n):
        if n <= 1:
            return 1
        return n*self.factorial(n-1)

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n += 1
        if n < 2:
            return 0
        arePrimes = n*[True]
        arePrimes[0] = False
        arePrimes[1] = False
        res = []
        for i in range(2, n):
            if arePrimes[i] == True:
                res.append(i)
                j = 2
                while i*j < n:
                    arePrimes[i*j] = False
                    j += 1
        return len(res)
