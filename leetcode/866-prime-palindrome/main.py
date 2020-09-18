"""
    1st: dynamic prgoramming
    - generate the primes from 1 to 15*N

    Time    O(Nlog(logN)) https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    Space   O(N)
    LTE
"""


class Solution(object):
    def primePalindrome(self, N):
        if N < 2:
            return 2
        M = 15*N
        arePrimes = M*[True]
        arePrimes[0] = False
        arePrimes[1] = False
        for i in range(2, M):
            if arePrimes[i] == True:

                if self.isPalindrome(i) and i >= N:
                    return i

                j = 2
                while i*j < M:
                    arePrimes[i*j] = False
                    j += 1
        return 2

    def isPalindrome(self, num):
        s = str(num)
        return s == s[::-1]


"""
    2nd: math
    - I dont think an interviwer expects a candidate to think in a math way
    - Our brute force works based on a fact that all 8 digit palindromes are not prime
    - So we can skip all 8 digit numbers, and jump to the 9 digit numbers

    ref:
    - https://leetcode.com/problems/prime-palindrome/solution/

    Time    O(NlogN)
    Space   O(1)
    532 ms, faster than 49.12%
"""


class Solution(object):
    def primePalindrome(self, N):
        while True:
            if self.isPalindrome(N) and self.isPrime(N):
                return N
            N += 1
            # all 8 digit palindromes are not prime, jump to 9 digit numbers
            if 10**7 < N < 10**8:
                N = 10**8

    def isPrime(self, num):
        isPrime = True
        for i in range(2, int(num**.5) + 1):
            if num % i == 0:
                isPrime = False
                break
        return num > 1 and isPrime == True

    def isPalindrome(self, num):
        s = str(num)
        return s == s[::-1]
