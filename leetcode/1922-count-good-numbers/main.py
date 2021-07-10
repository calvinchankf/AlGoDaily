"""
    1st: math, fast power
    - the brute force approach is to do muliplication
        if N = 11,
        res = 5 * 4 * 5 * 4 * 5 * 4 * 5 * 4 * 5 * 4 * 5
            = 5^6 * 4^5
    - since N would be large, we should do fast power(leetcode 50)

    Time    O(logN)
    Space   O(logN)
    36 ms, faster than 25.00%
"""


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        half = n // 2
        if n % 2 == 0:
            res = self.fastPower(5, half) * self.fastPower(4, half)
        else:
            res = self.fastPower(5, half+1) * self.fastPower(4, half)
        res %= 10**9 + 7
        return res

    def fastPower(self, x, n):
        if n == 0:
            return 1
        mid = n // 2
        temp = self.fastPower(x, mid)
        if n % 2 == 0:
            res = temp * temp
            res %= 10**9 + 7
            return res
        res = temp * temp * x
        res %= 10**9 + 7
        return res
