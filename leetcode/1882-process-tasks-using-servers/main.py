
from heapq import *

"""
    1st: min-heap
    - learned from others
    - use 2 min-heaps, one for available servers, another one for unavailable
    - as timeframe moves forward
        - update the availables and unavailables
        - put the current task into the smallest-weighted server

    ref:
    - https://leetcode.com/problems/process-tasks-using-servers/discuss/1239821/Two-MinHeaps-Explained

    Time    O(TlogS)
    Space   O(S)
    2104 ms, faster than 20.00%
"""


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        availables = [(servers[i], i)
                      for i in range(len(servers))]  # (weight, index)
        unavailables = []       # (time, weight, index)
        heapify(availables)
        res = []
        cur = 0
        for i in range(len(tasks)):
            t = tasks[i]
            cur = max(i, cur)

            # if no servers available, peek the earliest available time from busy servers
            if len(availables) == 0:
                cur = unavailables[0][0]

            # pop the servers if they finished their task
            while len(unavailables) > 0 and cur >= unavailables[0][0]:
                time, weight, idx = heappop(unavailables)
                heappush(availables, (weight, idx))

            # put the current task into the smallest-weighted server
            weight, idx = heappop(availables)
            heappush(unavailables, (cur + t, weight, idx))
            res.append(idx)
        return res
