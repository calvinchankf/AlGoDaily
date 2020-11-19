
from typing import List

"""
    1st: array

    Time    O(N)
    Space   O(1)
    60 ms, faster than 50.00%
"""
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        res = ''
        resCount = 0
        for i in range(n):
            c = keysPressed[i]
            t = releaseTimes[i]
            if i > 0:
                t -= releaseTimes[i-1]
            if t > resCount:
                res = c
                resCount = t
            elif t == resCount and c > res:
                res = c
        return res

s = Solution()

a = [9,29,49,50]
b = "cbcd"
print(s.slowestKey(a, b))

a = [12,23,36,46,62]
b = "spuda"
print(s.slowestKey(a, b))