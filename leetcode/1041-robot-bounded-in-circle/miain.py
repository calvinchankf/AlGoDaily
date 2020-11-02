"""
    1st: math
    - there are 2 cases that the path will form a cycle
        1. the path form the origin
        2. the end of a path doesnt face to north, so that if we repeat the instructions at most 4 times the final destination will be the origin


    Time    O(N)
    Space   O(1)
    20 ms, faster than 69.53%
"""


class Solution(object):
    def isRobotBounded(self, instructions):
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # start at 0,0 facing north
        x = y = 0
        facing = 0
        for inst in instructions:
            if inst == "R":
                facing = (facing + 1) % 4
            elif inst == "L":
                facing = (facing + 3) % 4
            else:
                x += directions[facing][0]
                y += directions[facing][1]
        return (x == 0 and y == 0) or facing != 0
