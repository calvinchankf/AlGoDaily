"""
    1st: brute force
    - sort the get the min and max year <= the dataset is small, we get also use 1950 and 2050 as the boundary
    - for each year, count the people who are alive

    Time    O(MN) M: years, N: logs
    Space   O(1)
    52 ms, faster than 65.62%
"""


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        left = logs[0][0]
        right = logs[-1][1]
        res = left
        maxCount = 0
        for i in range(left, right+1):
            count = 0
            for s, e in logs:
                if s <= i < e:
                    count += 1
            if count > maxCount:
                res = i
                maxCount = count
        return res
