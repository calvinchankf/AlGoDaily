"""
    1st approach: dynamic programming, learned from others
    - the basic idea is that when we pick a color, we should consider add up the cost from previous remaining colors
    e.g. pick red, consider previous cost from green and blue
    
    red = costs[i][0] + min(blue, green)

	- https://www.youtube.com/watch?v=fZIsEPhSBgM&t=1s

	Time	O(N)
	Space	O(3)
	44 ms, faster than 74.44% 
"""


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        red, blue, green = 0, 0, 0
        for x, y, z in costs:
            nextRed = x + min(blue, green)
            nextBlue = y + min(red, green)
            nextGreen = z + min(red, blue)
            red, blue, green = nextRed, nextBlue, nextGreen
        return min(red, blue, green)


a = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(Solution().minCost(a))

"""
    2nd: in-place
    - same logic as the 1st approach

    Time    O(N)
    Space   O(1)
    56 ms, faster than 81.87%
"""


class Solution:
    def minCost(self, costs) -> int:
        if len(costs) == 0:
            return 0
        for i in range(1, len(costs)):
            x, y, z = costs[i]
            costs[i][0] = x + min(costs[i-1][1], costs[i-1][2])
            costs[i][1] = y + min(costs[i-1][0], costs[i-1][2])
            costs[i][2] = z + min(costs[i-1][0], costs[i-1][1])
        return min(costs[-1])


"""
    variation: min -> max if the question is something like
    e.g. getting the max profit by painting the houses in non-adjacent colors
"""
