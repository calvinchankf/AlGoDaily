import sys

"""
    1st: coin change
    Time    O(N^2) but k <= 10^9...
    Space   O(N)
    TLE 26 / 503 test cases passed
"""


class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        cands = self.fibonacciNumebersUntilK(k)
        print(cands)
        return self.coinChange(cands, k)

    def fibonacciNumebersUntilK(self, k):
        fbnc = [1, 1]
        while True:
            temp = fbnc[-2] + fbnc[-1]
            if temp > k:
                break
            fbnc.append(temp)
        return fbnc

    def coinChange(self, coins, amount):
        coins = sorted(coins)
        dp = (amount+1)*[0]
        for i in range(1, amount+1):
            minSteps = sys.maxsize
            for coin in coins:
                remain = i-coin
                if remain < 0:
                    break
                minSteps = min(minSteps, dp[remain])
            dp[i] = minSteps + 1
        if dp[amount] >= sys.maxsize:
            return -1
        return dp[amount]


s = Solution()

print(s.fibonacciNumebersUntilK(100))
print(s.findMinFibonacciNumbers(100000))

print("-----")


"""
    2nd: greedy
    - subtract a Fibonacci number from the current number and repeat again the process until we reach to zero
    - its guaranteed that the path is minimum because the diff is increasing for every 2 continguous fibonacci numbers(after f(2))
    e.g.
    nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    diff =   0  1  1  2  3  5   8   13  21  34
    Time    O(N^2) but k <= 10^9...
    Space   O(N)
    TLE 26 / 503 test cases passed
"""


class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        cands = self.fibonacciNumebersUntilK(k)
        res = []
        remain = k
        while remain > 0:
            if remain - cands[-1] >= 0:
                res.append(cands[-1])
                remain -= cands[-1]
            else:
                cands.pop()
        return len(res)

    def fibonacciNumebersUntilK(self, k):
        fbnc = [1, 1]
        while True:
            temp = fbnc[-2] + fbnc[-1]
            if temp > k:
                break
            fbnc.append(temp)
        return fbnc


s = Solution()

print(s.findMinFibonacciNumbers(100))
print(s.findMinFibonacciNumbers(100000))
