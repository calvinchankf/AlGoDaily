"""
    1st: math
    - similar to lc732, l094, 1109, 1589, 1854
    - typical range counting technique (line sweep) to deal with values on a range
    - basically we can just use the prefix-sum concept to mark the start and the end of each interval

    Time    O(2n)
    Space   O(n)
    48 ms, faster than 71.10%
"""


class Solution(object):
    def carPooling(self, trips, capacity):
        n = 0
        for c, s, e in trips:
            n = max(n, e)
        occupiedCounts = (n + 1) * [0]

        # range counting technique
        for c, s, e in trips:
            occupiedCounts[s] += c
            occupiedCounts[e] -= c
        for i in range(1, n+1):
            occupiedCounts[i] = occupiedCounts[i-1] + occupiedCounts[i]

        maxCount = 0
        for i in range(n+1):
            maxCount = max(maxCount, occupiedCounts[i])
        return maxCount <= capacity


s = Solution()

a = [[5, 4, 7], [7, 4, 8], [4, 1, 8]]
b = 17
print(s.carPooling(a, b))
