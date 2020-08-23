class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        1st approach: prefix sum
        Time O(n^2)
        Space O(n)
        TLE
        """
        res = 0
        layer = []
        for i in range(len(nums)):
            newLayer = []
            for j in range(len(layer)):
                temp = layer[j] + nums[i]
                newLayer.append(temp)
                if temp == k and i-j+1 > res:
                    res = i-j+1
            newLayer.append(nums[i])
            if nums[i] == k and 1 > res:
                res = 1
            layer = newLayer
        return res


"""
    2nd approach: zero sum subarray
    - this question is fucking similar to leetcode523, 525, 560, 930, 1124, 1171
    - learned from others: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/77807/Clean-python-solution-one-pass
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: index of the previous sum
    - if currentSum - target in the hastable, the result is currentIndex - hastable[previous sum]

    ref:
    - https://www.youtube.com/watch?v=hLcYp67wCcM

    Time O(n)
    Space O(n) hashtable
    36ms beats 100%
"""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        res = 0
        acc = 0
        # key: previous sum, value: index of the previous sum
        ht = {}
        for i in range(len(nums)):
            acc += nums[i]
            if acc == k:
                res = i+1
            elif acc-k in ht:
                res = max(res, i-ht[acc-k])
            if acc not in ht:
                ht[acc] = i

        return res


print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))
print(Solution().maxSubArrayLen([-2, -1, 2, 1], 1))
print(Solution().maxSubArrayLen([-2, -1, 2, 1, 100], 100))
print(Solution().maxSubArrayLen([-2, -1, 2, 100, 1], 100))
print(Solution().maxSubArrayLen([-2, -1, 2, 1000], 99))
