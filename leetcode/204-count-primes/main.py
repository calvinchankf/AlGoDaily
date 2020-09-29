"""
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        isPrime = (n)*[True]
        isPrime[0] = False
        isPrime[1] = False
        res = 0
        for i in range(n):
            if isPrime[i] == True:
                res += 1
                j = 2
                while i*j < n:
                    isPrime[i*j] = False
                    j += 1
        return res


print(Solution().countPrimes(10))
print(Solution().countPrimes(101))

"""
    followup: print the primes
"""


class Solution(object):
    def printPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
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


print(Solution().printPrimes(10))
print(Solution().printPrimes(101))
