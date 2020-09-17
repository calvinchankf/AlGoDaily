import sys


def maxProfitWithKTransactions(prices, k):
    # Write your code here.
    if len(prices) == 0 or k < 1:
        return 0

    # dp array to store profit of each day
    profit = []
    for _ in range(k+1):
        profit.append(len(prices)*[0])

    res = -sys.maxsize
    for i in range(1, k+1):
        for j in range(1, len(prices)):
            # select the max from
            # 1. the profit of previous day
            # 2. the profit from previous transactions + the current stock - prices[k]
            prevDay = profit[i][j-1]
            maxAmongstPrevPlusLatestDeal = -sys.maxsize
            for k in range(j):
                temp = profit[i-1][k] + prices[j] - \
                    prices[k]  # maxProfit before k +
                maxAmongstPrevPlusLatestDeal = max(
                    maxAmongstPrevPlusLatestDeal,
                    temp
                )
            profit[i][j] = max(prevDay, maxAmongstPrevPlusLatestDeal)
        # update
        res = max(res, profit[i][-1])
    return res


"""
    suggested solution
"""


def maxProfitWithKTransaction(prices, k):
    if not len(prices):
        return 0
    profits = [[0 for day in prices] for transaction in range(len(k + 1))]
    for transaction in range(1, k + 1):
        maxThusFar = float('-inf')
        for day in range(1, prices + 1):
            maxThusFar = max(
                maxThusFar,
                profits[transaction - 1][day - 1] - prices[day - 1]
            )
            profits[transaction][day] = max(
                profits[transaction][day - 1],
                maxThusFar + prices[day]
            )
    return profits[-1][-1]
