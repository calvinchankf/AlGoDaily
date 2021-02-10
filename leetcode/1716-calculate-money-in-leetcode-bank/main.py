"""
    1st: math

    Time    O(N/7)
    Space   O(1)
    28 ms, faster than 95.78%
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        div = n // 7
        mod = n % 7
        a = self.calA(div)
        b = (1 + mod) * mod // 2 + div * mod
        return a + b

    def calA(self, n):
        total = 0
        for i in range(n):
            total += 28 + 7*i
        return total
