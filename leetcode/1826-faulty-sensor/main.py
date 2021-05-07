"""
    1st: array
    - similar to one edit distance

    Time    O(N)
    Space   O(1)
    40 ms, faster than 100.00%
"""


class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        for i in range(n-1):
            if sensor1[i] == sensor2[i]:
                continue
            if tuple(sensor1[i:-1]) == tuple(sensor2[i+1:]):
                return 1
            if tuple(sensor1[i+1:]) == tuple(sensor2[i:-1]):
                return 2
        return -1
