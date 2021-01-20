import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        1st approach:
        - use the algo from Best Time to Buy and Sell Stock I
        - for each i, calculate the maxProfit(prices[:i]) + maxProfit(prices[i:]) and put them into the result

        Time    O(n^2)
        Space   O(1)
        LTE
        """
        result = 0
        for i in range(len(prices)):
            left = self.maxProfitWithin(prices[:i])
            right = self.maxProfitWithin(prices[i:])
            if left + right > result:
                result = left + right
        return result

    def maxProfitWithin(self, prices):
        if len(prices) < 2:
            return 0
        bay = prices[0]
        diff = 0
        for price in prices:
            if price < bay:
                bay = price
            if price - bay > diff:
                diff = price - bay
        return diff


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([2, 4]))
print(Solution().maxProfit([2, 4, 1]))
print(Solution().maxProfit([2, 4, 1, 4]))

print("------")


class Solution(object):
    def maxProfit(self, prices):
        """
        2nd approach: optimize the 1st approach
        - try to compensate some space for optimization
        - save the maxprofit on each day when we traverse forward
        - save the maxprofit on each day when we traverse backward
        - the result will be the max sum of profit on day i, which is forward[i]+backward[i]
        - see ./idea.jpeg

        Time    O(4N)
        Space   O(2N)
        1776 ms, faster than 12.55%
        """
        if len(prices) < 2:
            return 0
        n = len(prices)
        dip = sys.maxsize
        forwardDiff = 0
        forwardDiffs = []
        for price in prices:
            dip = min(dip, price)
            forwardDiff = max(forwardDiff, price - dip)
            forwardDiffs.append(forwardDiff)

        peak = -sys.maxsize
        backwardDiff = 0
        backwardDiffs = []
        for i in range(n-1, -1, -1):
            price = prices[i]
            peak = max(peak, price)
            backwardDiff = max(backwardDiff, peak - price)
            backwardDiffs.append(backwardDiff)
        backwardDiffs = backwardDiffs[::-1]

        result = 0
        for i in range(n):
            result = max(result, forwardDiffs[i] + backwardDiffs[i])
        return result


print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([2, 4]))
print(Solution().maxProfit([2, 4, 1]))
print(Solution().maxProfit([2, 4, 1, 4]))
