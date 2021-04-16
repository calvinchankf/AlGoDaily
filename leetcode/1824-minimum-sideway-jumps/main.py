"""
    1st: BFS + hashset
    - for every point, there are 3 possibilities to move forward
    - dont step on the obstacles
    - dont step on the points you visited

    Time    O(3N) there are at most 3N cells
    Space   O(3N)
    8288 ms, faster than 5.42%
"""


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        q = [(0, 1, 0)]
        seen = set()
        while len(q) > 0:
            point, lane, jumps = q.pop(0)
            if point == n-1:
                return jumps
            if obstacles[point]-1 == lane:
                continue
            key = (point, lane)
            if key in seen:
                continue
            seen.add(key)
            q.append((point + 1, lane, jumps))
            q.append((point, (lane + 1) % 3, jumps + 1))
            q.append((point, (lane + 2) % 3, jumps + 1))
        return 0


"""
    2nd: BFS + hashset
    - same as 1st but only put visitable points into the queue

    Time    O(3N) there are at most 3N cells
    Space   O(3N)
    7264 ms, faster than 10.09%
"""


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        q = [(0, 1, 0)]
        seen = set()
        while len(q) > 0:
            point, lane, jumps = q.pop(0)
            if point == n-1:
                return jumps
            key = (point, lane)
            if key in seen:
                continue
            seen.add(key)
            if obstacles[point+1]-1 != lane:
                q.append((point + 1, lane, jumps))
            if obstacles[point]-1 != (lane + 1) % 3:
                q.append((point, (lane + 1) % 3, jumps + 1))
            if obstacles[point]-1 != (lane + 2) % 3:
                q.append((point, (lane + 2) % 3, jumps + 1))
        return 0


"""
    2nd: dynamic programming, bottom up
    - there are 3 lanes only, and there are no stones on the first point so we can use [1,0,1] to represent the costs
    - at every point, use the previous cost, and the cost from the neighbours for calculation

    Time    O(3N)
    Space   O(3) -> O(1)
    3680 ms, faster than 63.44%
"""


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [1, 0, 1]
        for i in range(1, n):
            laneIdx = obstacles[i] - 1
            if laneIdx > -1:
                dp[laneIdx] = 2**32
            for j in range(3):
                if j != laneIdx:
                    dp[j] = min(dp[j], dp[(j+1) % 3] + 1, dp[(j+2) % 3] + 1)
        return min(dp)
