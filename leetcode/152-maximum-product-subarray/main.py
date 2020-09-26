import sys

"""
    3rd approach: Kadan's algorithm
    - idea similar to leetcode 53:maximum subarray, 1567
    - for each item, store the max&mix among itself, or extend the previous max&min with itself
      e.g. dp[i] chooses between dp[i-1]+nums[i] and nums[i]
    - the result is the largest dp[i]
    - see ./idea.jpeg

    Time	O(n)
    Space	O(n)
    56 ms, faster than 28.11%
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minP = sys.maxsize
        maxP = -sys.maxsize
        res = -sys.maxsize
        for num in nums:
            if num > 0:
                minP = min(minP*num, num)
                maxP = max(maxP*num, num)
            else:
                temp = minP
                minP = min(maxP*num, num)
                maxP = max(temp*num, num)
            res = max(res, maxP)
        return res


a = [2, 3, -2, 4, -3]
print(Solution().maxProduct(a))

print("-----")

"""
    followup: print that array
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minP = sys.maxsize
        minArr = []
        maxP = -sys.maxsize
        maxArr = []
        res = -sys.maxsize
        resArr = []
        for num in nums:
            if num > 0:
                # minP = min(minP*num, num)
                # maxP = max(maxP*num, num)
                # minProduct
                if minP*num < num:
                    minP = minP*num
                    minArr.append(num)
                else:
                    minP = num
                    minArr = [num]
                # maxProduct
                if maxP*num > num:
                    maxP = maxP*num
                    maxArr.append(num)
                else:
                    maxP = num
                    maxArr = [num]
            else:
                temp = minP
                tempArr = minArr
                # minProduct
                if maxP*num < num:
                    minP = maxP*num
                    # extend the minArr with maxArr+[nums[i]]
                    minArr = maxArr+[num]
                else:
                    minP = num
                    minArr = [num]
                # maxProduct
                if temp*num > num:
                    maxP = temp*num
                    # extend the maxArr with minArr+[nums[i]]
                    maxArr = tempArr+[num]
                else:
                    maxP = num
                    maxArr = [num]
            if maxP > res:
                res = maxP
                resArr = maxArr[:]

        return res, resArr


a = [2, 3, -2, 4, -3]
print(Solution().maxProduct(a))
