"""
    1st: math?
    - for every customer, calculate it's start time with the current time

    Time    O(N)
    Space   O(1)
    1020 ms, faster than 33.33%
"""


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total = 0
        t = customers[0][0]
        for i in range(n):
            s, d = customers[i]
            t = max(t, s) + d
            total += t - s
        return total / n
