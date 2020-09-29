"""
    2nd approach: recurisve split + hashtable(avoid redundant calculation)

               2^10
            2^5 * 2^5
        2^2 * 2^3 * 2^2 * 2^3
    2^2 * 2^2 * 2 * 2^2 * 2^2 * 2

    Time    O(logn)
    Space   O(logn)
    24 ms, faster than 39.07%
"""


class Solution(object):
    def __init__(self):
        self.cache = {}

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.helper(x, -n)
        return self.helper(x, n)

    def helper(self, x, n):
        if n in self.cache:
            return self.cache[n]
        if n == 1:
            return x
        left = n/2
        right = n-left
        temp = self.helper(x, left) * self.helper(x, right)
        self.cache[n] = temp
        return temp


print(Solution().myPow(2.0, 10))
print(Solution().myPow(2.1, 3))
print(Solution().myPow(2, -2))
print(Solution().myPow(2, 0))
print(Solution().myPow(2, 1))

print("----------")

"""
    3rd approach: optimze 2nd
    - same logic to split the numbers

               2^10
            2^5 * 2^5
        2^2 * 2^3 * 2^2 * 2^3
    2^2 * 2^2 * 2 * 2^2 * 2^2 * 2

    Time    O(logn)
    Space   O(logn) recursion tree
    20 ms, faster than 96.88%
"""


class Solution(object):

    def myPow(self, x, n):
        if n >= 0:
            return self.dfs(x, n)
        return 1 / self.dfs(x, -n)

    def helper(self, x, n):
        # if n == 0, x^0 = 1
        if n == 0:
            return 1
        # e.g.1 n = 5, n//2 = 2*2
        # e.g.2 n = 4, n//2 = 2*2
        # e.g.3 n = 1, n//2 = 0
        half = self.dfs(x, n//2)
        if n % 2 == 0:
            # since n is an even, return 2^2 * 2^2
            return half * half
        # since n is an odd, return 2^2 * 2^2 * 2
        # base case when n = 1, return 1 * 1 * x
        return half * half * x


print(Solution().myPow(2.0, 10))
print(Solution().myPow(2.1, 3))
print(Solution().myPow(2, -2))
print(Solution().myPow(2, 0))
print(Solution().myPow(2, 1))
