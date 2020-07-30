"""
    1st: math
    - set 00:00 as a fixed position
    1. calculate the angle between the 00:00 and the hour
    2. calculate the angle between the 00:00 and the minute
    - calculate the diff between 1) and 2)

    Time    O(1)
    Space   O(1)
    24 ms, faster than 93.34%
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = minutes
        h = (hour % 12) * 5 + m / 60 * 5
        cand = abs(m - h) * 180 / 30
        if cand > 180:
            return 360 - cand
        return cand
