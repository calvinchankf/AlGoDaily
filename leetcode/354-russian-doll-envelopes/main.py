from typing import List

"""
    1st: brute force dp

    Time    O(N^2)
    Space   O(N)
    LTE 84 / 85 test cases passed.
"""


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 0:
            return 0
        nums = envelopes[:]
        nums.sort(key=lambda x: x[0] * x[1])
        # print(nums)
        dp = n * [0]
        for i in range(n):
            maxPrev = 0
            for j in range(i):
                if nums[j][0] < nums[i][0] and nums[j][1] < nums[i][1]:
                    maxPrev = max(maxPrev, dp[j])
            dp[i] = maxPrev + 1
        # print(dp)
        return max(dp)


s = Solution()

# 4
a = [[5, 4], [8, 7], [8, 3], [6, 4], [8, 8], [6, 7], [
    2, 3], [1, 10], [3, 9], [10, 2], [10, 4], [10, 5]]
print(s.maxEnvelopes(a))
