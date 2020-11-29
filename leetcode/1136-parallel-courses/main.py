"""
    1st: topo sort

    Time    O(N + E) E: number of edges
    Space   O(N)
    272 ms, faster than 45.79%
"""


class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        connections = {}
        indegrees = {}
        for x in range(1, N+1):
            connections[x] = []
            indegrees[x] = 0
        # get all the adjacents list and indegree
        for src, dest in relations:
            connections[src].append(dest)
            indegrees[dest] += 1
        # get the nodes with 0 indegree
        queue = []
        for node in indegrees:
            if indegrees[node] == 0:
                queue.append((node, 1))
        # dequeue node from the queue and put it into the result
        res = 0
        while len(queue) > 0:
            node, depth = queue.pop(0)
            res = max(res, depth)
            children = connections[node]
            for child in children:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    queue.append((child, depth + 1))
        # return [] if there is a cycle
        for key in indegrees:
            if indegrees[key] > 0:
                return -1
        return res
