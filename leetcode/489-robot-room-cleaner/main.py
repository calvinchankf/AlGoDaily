"""
    learned from others: dfs
    - https://leetcode.com/problems/robot-room-cleaner/solution/


    Time    O(4^n) each cell has 4 direction to go at max
    Space   O(n) visited hashset
    100 ms, faster than 27.00%
"""


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [
            (-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)
        ]
        visited = set()

        # go back to the previous position
        # and face to the same direction
        # as if the way when the robot saw this grid[i][j]
        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        # dfs
        def explore(x, y, d):
            robot.clean()
            visited.add((x, y))
            for i in range(4):
                # i want the robot to go the original direction
                # instead of checking up,right,down.left every time it arrives to a new grid[i][j]
                new_d = (d + i) % 4
                # new grid coordinate
                newX = x + directions[new_d][0]
                newY = y + directions[new_d][1]
                # if unvisited and can move, explore there (with the same direction)
                if (newX, newY) not in visited and robot.move():
                    explore(newX, newY, new_d)
                    goback()
                # always turn right
                robot.turnRight()
        explore(0, 0, 0)
