"""
    1st: divide + conquer
    - reuse lc50
    - in fact, e.g. a^[b, c, d] = a^(b*100 + c*10 + d), therefore we can just "power up" the preceding result when we iterate

    Time    O(B log(Bi))
    Space   O(log(Bi)) <- recursion tree
    124 ms, faster than 44.73%
"""


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for x in b:
            res = (res**10) * self.power(a, x) % 1337
        return res

    def power(self, x: int, n: int) -> int:
        # if n == 0, x^0 = 1
        if n == 0:
            return 1
        # e.g.1 n = 5, left = 2
        # e.g.2 n = 4, left = 2
        # e.g.3 n = 1, left = 0
        left = n // 2
        # e.g.1,2 temp = 2^2
        temp = self.power(x, left)
        if n % 2 == 0:
            # since n is an even, return 2^2 * 2^2
            return temp * temp
        # since n is an odd, return 2^2 * 2^2 * 2
        # base case when n = 1, return 1 * 1 * x
        return temp * temp * x


"""
    2nd approach: recurisve split + hashtable(avoid redundant calculation)

               2^10
            2^5 * 2^5
        2^2 * 2^3 * 2^2 * 2^3
    2^2 * 2^2 * 2 * 2^2 * 2^2 * 2

    Time    O(B log(Bi)) its will be a bit faster since we cache
    Space   O(log(Bi)) <- recursion tree
    100 ms, faster than 61.66% 
"""


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        self.cache = {}
        res = 1
        for x in b:
            res = (res**10) * self.power(a, x) % 1337
        return res

    def power(self, x, n):
        if n in self.cache:
            return self.cache[n]
        if n == 0:
            return 1
        if n == 1:
            return x
        left = n // 2
        right = n - left
        temp = self.power(x, left) * self.power(x, right)
        self.cache[n] = temp
        return temp
