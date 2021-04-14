import random

"""
    1st: rejection sampling
    - learned from others
    - the area of the wrapping square = 4RR
    - the area of the circle = 3.14RR
    - so the pobrability we get a point inside the circle = 3.14/4 = 0.785
    - so the average number of times we get a point with randPoint() = 1/0.785 = 1.274

    ref:
    - https://leetcode.com/problems/generate-random-point-in-a-circle/solution/

    Time    O()
    Space   O(1)
    152 ms, faster than 47.85%
"""


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(self.xc-self.radius, self.xc+self.radius)
            y = random.uniform(self.yc-self.radius, self.yc+self.radius)
            if (x - self.xc)**2 + (y - self.yc)**2 <= self.radius**2:
                return [x, y]
