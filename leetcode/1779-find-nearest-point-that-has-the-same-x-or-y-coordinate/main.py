"""
    1st: math

    Time    O(N)
    Space   O(N)
    700 ms, faster than 100.00%
"""
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        resD = 2**32
        for i in range(len(points)):
            _x, _y = points[i]
            if _x == x or _y == y:
                d = abs(_x - x) + abs(_y - y)
                if d < resD:
                    resD = d
                    res = i
        return res