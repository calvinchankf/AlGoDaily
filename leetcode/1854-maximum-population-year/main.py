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


"""
    2nd: line sweep
    - similar to lcl094, 1109, 1589, 1854

    concept:

    e.g. [[1991, 1994], [1992, 1996], [1993, 1995], [1996, 1998], [1997, 1999]]

    1990    1991    1992    1993    1994    1995    1996    1997    1998    1999    2000 <- year
            +1                      -1
                    +1                              -1
                            +1              -1
                                                    +1              -1
                                                            +1              -1
    ------------------------------------------------------------------------------------
            1       1       1       -1      -1      0       1       -1      -1          <- the diff in every year
            1       2       3       2       1       1       2       1       0           <- prefixSum of the diffs means the count in every year
                            ^ result = 1993 in which the most people are alive
    
    Time    O(N)
    Space   O(N)
    44 ms, faster than 86.00%
"""


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        counts = 2501 * [0]
        for s, e in logs:
            counts[s] += 1
            counts[e] -= 1
        for i in range(1950, 2501):
            counts[i] += counts[i-1]
        res = -1
        maxCount = 0
        for i in range(1950, 2501):
            if counts[i] > maxCount:
                res = i
                maxCount = counts[i]
        return res
