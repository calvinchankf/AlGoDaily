from typing import List
import sys

"""
    1st: sort
    - learned from others

    ref:
    - https://leetcode.com/problems/two-city-scheduling/solution/

    Time    O(NlogN)
    Space   O(1)
    36 ms, faster than 82.68%
"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by a gain which company has
        # by sending a person to city A and not to city B
        costs.sort(key=lambda x: x[0] - x[1])
        total = 0
        half = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A
        # and the others to the city B
        for i in range(half):
            total += costs[i][0] + costs[i + half][1]
        return total


s = Solution()

a = [[10, 20], [30, 200], [400, 50], [30, 20]]
print(s.twoCitySchedCost(a))

a = [[10, 20], [30, 200], [400, 50], [20, 30]]
print(s.twoCitySchedCost(a))

a = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
print(s.twoCitySchedCost(a))

print('-----')

"""
    2nd: dynamic programming
    - recursion to get all the combinations
    - use a hashtable to avoid redundant calculation to optimize the speed from O(2^N) tp O(N^2)

    Time    O(N^2)
    Space   O(N^2)
    128 ms, faster than 5.15%
"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        self.cached = {}
        return self.dfs(costs, 0, 0, 0)

    def dfs(self, costs, count_a, count_b, index):
        if (count_a, count_b, index) in self.cached:
            return self.cached[(count_a, count_b, index)]
        if count_a == count_b == len(costs) // 2:  # Valid division of people
            return 0
        if index == len(costs):
            return sys.maxsize  # Invalid division of people
        minCost = min(
            costs[index][0] + self.dfs(costs, count_a + 1, count_b, index + 1),
            costs[index][1] + self.dfs(costs, count_a, count_b + 1, index + 1)
        )
        self.cached[(count_a, count_b, index)] = minCost
        return minCost
