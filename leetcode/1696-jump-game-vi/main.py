"""
    2nd: dynamic programming + dequeue
    - maintain a monotonic decreasing dequeue
    - dp[i] = nums[i] + dp[index of deq[0]]
    - when the index of deq[0]

    e.g. [1, -1, -2, 4,-7, 3] k = 2

    i   nums[i]     dp[i]   dequeue
    0   1           1       [1]
    1   -1          0       [1,0]
    2   -2          -1      [0,-1]
    3   4           4       [4]
    4   -7          -3      [4,-3]
    5   3           7       [7]

    ref:
    - https://www.youtube.com/watch?v=M_PzYd59_kk
    - https://leetcode.com/problems/jump-game-vi/solution/

    Time    O(N)
    Space   O(K)
    980 ms, faster than 41.95%
"""


class Solution(object):
    def maxResult(self, nums, k):
        n = len(nums)
        dp = n * [0]
        first = nums[0]
        dp[0] = first
        deq = [(first, 0)]  # [(val, idx), ...]
        for i in range(1, n):
            dp[i] = nums[i] + dp[deq[0][1]]
            if len(deq) > 0 and deq[0][1] + k <= i:
                deq.pop(0)
            while len(deq) > 0 and dp[i] >= dp[deq[-1][1]]:
                deq.pop()
            deq.append((dp[i], i))
        return dp[-1]
