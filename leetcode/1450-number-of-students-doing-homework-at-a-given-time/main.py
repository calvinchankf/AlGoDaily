"""
    1st: array iteration

    Time    O(N)
    Space   O(1)
    68 ms, faster than 33.33%
"""


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        n = len(startTime)
        for i in range(n):
            s = startTime[i]
            e = endTime[i]
            if s <= queryTime <= e:
                res += 1
        return res
