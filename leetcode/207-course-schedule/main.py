"""
    1st approach: topo ordering BFS with array

    Time    O(V+E)
    Space   O(V)
    80 ms, faster than 60.39%
    7may2019
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        connections = []
        indegrees = []
        for _ in range(numCourses):
            indegrees.append(0)
            connections.append([])

        for cur, prev in prerequisites:
            indegrees[cur] += 1
            connections[prev].append(cur)

        q = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)

        res = []
        while len(q) > 0:
            pop0 = q.pop(0)
            res.append(pop0)
            children = connections[pop0]
            for child in children:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)
        return len(res) == numCourses


print(Solution().canFinish(2, [[1, 0]]))
print(Solution().canFinish(2, [[0, 1], [1, 0]]))
print(Solution().canFinish(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]]))
print(Solution().canFinish(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3], [3, 5]]))
print("-----")

"""
    2nd approach: topo ordering BFS but with hashtable

    Time    O(V+E)
    Space   O(V)
    216 ms, faster than 20.38%
    28mar2019
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        connections = {}
        indegrees = {}
        for num in range(numCourses):
            connections[num] = []
            indegrees[num] = 0

        for cur, prev in prerequisites:
            indegrees[cur] += 1
            connections[prev].append(cur)

        q = []
        for x in indegrees:
            if indegrees[x] == 0:
                q.append(x)

        res = []
        while len(q) > 0:
            pop0 = q.pop(0)
            res.append(pop0)
            children = connections[pop0]
            for child in children:
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)

        return len(res) == numCourses


print(Solution().canFinish(2, [[1, 0]]))
print(Solution().canFinish(2, [[0, 1], [1, 0]]))
print(Solution().canFinish(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]]))
print(Solution().canFinish(
    6, [[4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3], [3, 5]]))
