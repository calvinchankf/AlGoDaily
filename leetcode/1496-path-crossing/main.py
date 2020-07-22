"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    28 ms, faster than 66.67%
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        m = {
            'N': (0, -1),
            'S': (0, 1),
            'W': (-1, 0),
            'E': (1, 0),
        }
        seen = set()
        x, y = 0, 0
        seen.add((x, y))
        for c in path:
            x += m[c][0]
            y += m[c][1]
            key = (x, y)
            if key in seen:
                return True
            seen.add(key)
        return False
