import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        1st approach: increasing sequence
        - keep track of the last item if the sequence is increasing
        - if the sequence decrease, sum the last-bay to the result and update the bay and last with the current price

        Time    O(n)
        Space   O(1)
        24 ms, faster than 97.73% 
        """
        if len(prices) < 2:
            return 0
        last = prices[0]
        bay = prices[0]
        res = 0
        for i in range(len(prices)):
            price = prices[i]
            if price >= last:
                last = price
                if i + 1 == len(prices):
                    res += last - bay
            else:
                res += last - bay
                bay = price
                last = price
        return res


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 5, 4, 3]))
print(Solution().maxProfit([1, 3]))
print(Solution().maxProfit([3, 1]))
print(Solution().maxProfit([1]))
print(Solution().maxProfit([1]))

print("-----------------------------------")

"""
    2nd approach: maintain the minVal
    - keep track of the minVal
    - if current value > minVal, add up the diff = prices[i] - minVal to the result, then reset the minVal

    Time    O(n)
    Space   O(1)
    52 ms, faster than 29.52%

    why it is slower than 1st: perform more += operation because it doesn't care abuot the increasing sequence
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        dip = sys.maxsize
        for p in prices:
            if p - dip > 0:
                res += p - dip
                dip = p
            dip = min(dip, p)
        return res


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 5, 4, 3]))
print(Solution().maxProfit([1, 3]))
print(Solution().maxProfit([3, 1]))
print(Solution().maxProfit([1]))
print(Solution().maxProfit([1]))

print("-----------------------------------")

"""
    3rd approach:
    - actually eery time when we see nums[i] > nums[i-1], we can just add the diff into the result

    Time    O(n)
    Space   O(1)
    48 ms, faster than 47.05%
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution().maxProfit([1, 2, 3, 4, 5]))
print(Solution().maxProfit([7, 6, 5, 4, 3]))
print(Solution().maxProfit([1, 3]))
print(Solution().maxProfit([3, 1]))
print(Solution().maxProfit([1]))
print(Solution().maxProfit([1]))
