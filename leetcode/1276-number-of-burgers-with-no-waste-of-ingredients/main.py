"""
    1st: math math math
    
    4X + 2Y = a
      X + Y = b
    
    Time    O(1)
    Space   O(1)
    36 ms, faster than 63.18%
"""


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        a = tomatoSlices
        b = cheeseSlices
        if a % 2 == 1 or b > a:
            return []
        x = (a - 2 * b) // 2
        y = b - x
        if x < 0 or y < 0:
            return []
        return [x, y]
