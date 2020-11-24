from typing import List
import sys

"""
    1st: sort
    - learned from others
    - first fill CityA, then the remaning people go to CityB

    e.g.1
    [[10,20],[30,200],[400,50],[30,20]]
    
    consider idx0, cityA is the way cheaper to go
    consider idx1, cityA is the way cheaper to go

    so we can sort the costs by diff btw going to cityA and cityB

    person1     person0   person3   person2
    ------------------------------------------
    [[30, 200], [10, 20], [30, 20], [400, 50]]
        -170        -10     10          350     <= diff


    e.g.2 
    [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]

    person0      person3     person5     person2     person1    person4
    -----------------------------------------------------------------------
    [[259, 770], [184, 139], [577, 469], [926, 667], [448, 54], [840, 118]]
        -551        45          108         259         394         722     <= diff
    
    ref:
    - https://leetcode.com/problems/two-city-scheduling/solution/
    - https://www.youtube.com/watch?v=3A98vh5zsqw

    Time    O(NlogN)
    Space   O(1)
    36 ms, faster than 82.68%
"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        total = 0
        n = len(costs) // 2
        for i in range(len(costs)):
            if i < n:
                total += costs[i][0]
            else:
                total += costs[i][1]
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

s = Solution()

a = [[10, 20], [30, 200], [400, 50], [30, 20]]
print(s.twoCitySchedCost(a))

a = [[10, 20], [30, 200], [400, 50], [20, 30]]
print(s.twoCitySchedCost(a))

a = [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]
print(s.twoCitySchedCost(a))

print('-----')


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        self.cached = {}
        return self.dfs(costs, 0, n, n)

    def dfs(self, costs, i, countA, countB):
        if countA == 0 and countB == 0:
            return 0
        if i == len(costs):
            return 2**32
        key = (countA, countB)
        if key in self.cached:
            return self.cached[key]
        left = self.dfs(costs, i+1, countA - 1, countB) + costs[i][0]
        right = self.dfs(costs, i+1, countA, countB - 1) + costs[i][1]
        self.cached[key] = min(left, right)
        return self.cached[key]
