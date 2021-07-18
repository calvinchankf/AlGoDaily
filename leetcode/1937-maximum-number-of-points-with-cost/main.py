"""
    1st: brute force DP

    Time    O(RCC)
    Space   O(RC)
    LTE
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        R, C = len(points), len(points[0])
        dp = []
        for _ in range(R):
            dp.append(C * [0])
        for j in range(C):
            dp[0][j] = points[0][j]
        for i in range(1, R):
            for j in range(C):
                maxToAdd = 0
                for k in range(C):
                    toAdd = dp[i-1][k] - abs(j - k)
                    maxToAdd = max(maxToAdd, toAdd)
                dp[i][j] = points[i][j] + maxToAdd
        return max(dp[-1])


"""
    2nd: DP
    - use the concept of left&right arrays
    - for every col
        - pre-compute the index to add
        - pre-compute the index to delete

    ref:
    - https://leetcode.com/problems/maximum-number-of-points-with-cost/discuss/1344888/C%2B%2B-dp-from-O(m-*-n-*-n)-to-O(m-*-n)

    Time    O(RC)
    Space   O(RC)
    2100 ms, faster than 100.00%
"""


class Solution(object):
    def maxPoints(self, points):
        R, C = len(points), len(points[0])
        dp = []
        for _ in range(R):
            dp.append(C * [0])
        for j in range(C):
            dp[0][j] = points[0][j]
        for i in range(1, R):
            left_dp = C * [-1]
            right_dp = C * [-1]

            left_dp[0] = dp[i-1][0]
            for k in range(1, C):
                left_dp[k] = max(left_dp[k-1], dp[i-1][k] + k)

            right_dp[-1] = dp[i-1][-1] - C + 1
            for k in range(C-2, -1, -1):
                right_dp[k] = max(right_dp[k+1], dp[i-1][k] - k)

            for j in range(C):
                dp[i][j] = max(left_dp[j] - j, right_dp[j] + j) + points[i][j]

        return max(dp[-1])
