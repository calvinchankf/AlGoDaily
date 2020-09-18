import sys

"""
    classic approach: dynamic programming
    
    ref: 
    https://www.youtube.com/watch?v=Pw6lrYANjz4

    Time    O(NKK)
    Space   O(n)
    MLE
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or k < 1:
            return 0

        # dp array to store profit on each day
        profit = []
        for _ in range(k+1):
            profit.append(len(prices)*[0])

        res = -sys.maxsize
        for i in range(1, k+1):
            for j in range(1, len(prices)):
                # select the max from either
                # 1. the profit on previous day
                # 2. the profit amongst (previous transactions until k + the current stock - prices[k])
                prevDay = profit[i][j-1]
                maxAmongstPrevPlusLatestDeal = -sys.maxsize
                for k in range(j):
                    temp = profit[i-1][k] + prices[j] - prices[k]
                    maxAmongstPrevPlusLatestDeal = max(
                        maxAmongstPrevPlusLatestDeal,
                        temp
                    )
                profit[i][j] = max(prevDay, maxAmongstPrevPlusLatestDeal)
            # update
            res = max(res, profit[i][-1])
        return res


s = Solution()

a = 2
b = [3, 2, 6, 5, 0, 3]
print(s.maxProfit(a, b))

a = 2
b = [5, 11, 3, 50, 60, 90]
print(s.maxProfit(a, b))

print("-----")

"""
    classic approach: dynamic programming
    
    ref: 
    https://www.youtube.com/watch?v=Pw6lrYANjz4

    Time    O(NKK)
    Space   O(n)
    TLE 209 / 211 test cases passed.
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or k < 1:
            return 0

        # dp array to store profit on each day
        profit = len(prices) * [0]

        res = -sys.maxsize
        for _ in range(k):
            nextProfit = len(prices) * [0]
            for j in range(1, len(prices)):
                # select the max from either
                # 1. the profit on previous day
                # 2. the profit amongst (previous transactions until k + the current stock - prices[k])
                prevDay = nextProfit[j-1]
                maxAmongstPrevPlusLatestDeal = -sys.maxsize
                for k in range(j):
                    temp = profit[k] + prices[j] - prices[k]
                    maxAmongstPrevPlusLatestDeal = max(
                        maxAmongstPrevPlusLatestDeal,
                        temp
                    )
                nextProfit[j] = max(prevDay, maxAmongstPrevPlusLatestDeal)
            # update
            profit = nextProfit
            res = max(res, profit[-1])
        return res


"""
    classic approach: dynamic programming
    
    ref: 
    https://www.youtube.com/watch?v=Pw6lrYANjz4

    Time    O(NKK)
    Space   O(n)
    TLE 209 / 211 test cases passed.
"""
s = Solution()

a = 2
b = [3, 2, 6, 5, 0, 3]
print(s.maxProfit(a, b))

a = 2
b = [5, 11, 3, 50, 60, 90]
print(s.maxProfit(a, b))


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k < 1:
            return 0

        # dp array to store profit on each day
        profits = len(prices) * [0]
        for _ in range(k):
            nextProfits = len(prices) * [0]
            maxThusFar = -sys.maxsize
            for j in range(1, len(prices)):
                maxThusFar = max(maxThusFar, profits[j-1] - prices[j - 1])
                nextProfits[j] = max(nextProfits[j - 1],
                                     maxThusFar + prices[j])
            profits = nextProfits
        return profits[-1]
