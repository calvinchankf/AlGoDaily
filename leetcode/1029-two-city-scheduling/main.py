from typing import List

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
