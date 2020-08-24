"""
    1st approach: Topological Ordering in DFS

    1. create a list to save to children for each node
    2. for each node, put the children in
        e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
        children list = [[], [0], [3], [], [3], [2,4,1]]
    3. use a hashtable to store the visited node, 1=visiting, 2=visited
    4. use a stack to store the nodes which no longer has unvisited children
    5. the result is the stack in the reversed order

    Time    O(V+E)
    Space   O(V)
    36ms beats 98.29%
"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # prepare a list to save to children for each node
        connections = []
        for i in range(numCourses):
            connections.append([])
        # iterate though the edges and put them into the corresponding node in the graph
        for prereq in prerequisites:
            prev, cur = prereq[1], prereq[0]
            connections[prev].append(cur)
        # iterate all the vertices
        seen = {}
        stack = []
        for i in range(numCourses):
            if i in seen:
                if seen[i] == 1:
                    return []
                elif seen[i] == 2:
                    continue
            if self.exploreVertex(connections, i, seen, stack) == False:
                return []
        # result is the stack in a reversed order
        res = []
        while len(stack) > 0:
            res.append(stack.pop())
        return res

    def exploreVertex(self, connections, curIdx, seen, stack):
        seen[curIdx] = 1
        children = connections[curIdx]
        for child in children:
            if child in seen:
                if seen[child] == 1:
                    return False
                elif seen[child] == 2:
                    continue
            if self.exploreVertex(connections, child, seen, stack) == False:
                return False
        seen[curIdx] = 2
        stack.append(curIdx)
        return True


print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2]]))

print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2], [5, 3]]))


print("---------------------------------------------")

"""
    2nd appraoch: Topological Ordering in BFS

    1. create a list to save to children for each node
    2. for each node, put the children in
        e.g. [4, 3], [1, 0], [5, 2], [5, 4], [5, 1], [2, 3]
        children list = [[], [0], [3], [], [3], [2,4,1]]
    3. count the indegree for each node(indegree = the number of incoming edges)
    4. put the nodes with 0 indegree into a queue
    5. if the queue is not empty, append the dequeued node to the result and in the same time decrement it's children's indegree
    6  after decrement, if there are nodes which has 0 indegree, put them into the queue
    7. do 6) and 7) until the queue becomes empty
    8. need a 'cnt' to check if there is a cycle(for detail: see comment)

    Time    O(V+E)
    Space   O(V)
    32ms beats 100%
"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # prepare a list to save to children for each node
        connections = []
        indegrees = []
        for i in range(numCourses):
            connections.append([])
            indegrees.append(0)
        # iterate though the edges and put them into the corresponding node in the connections
        for cur, prev in prerequisites:
            connections[prev].append(cur)
            indegrees[cur] += 1
        # put the nodes which has no incoming edges
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        # 0 indegree nodes are the result
        res = []
        while len(queue) > 0:
            head = queue.pop(0)
            res.append(head)
            children = connections[head]
            for child in children:
                # subtract 1 for all destinations which the current node points(prereq) to
                indegrees[child] -= 1
                # if indegree of that child is 0, out it to the queue
                if indegrees[child] == 0:
                    queue.append(child)

        if len(res) != numCourses:
            return []
        return res


print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2]]))

print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2], [5, 3]]))

print("---------------------------------------------")


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        3rd approach: topo sort with hashtable but not int array

        Time    O(V+E)
        Space   O(V)
        196 ms, faster than 19.02%
        28mar2019
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

        if len(res) != numCourses:
            return []
        return res


print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2]]))

print(Solution().findOrder(
    6, [[3, 4], [0, 1], [2, 5], [4, 5], [1, 5], [3, 2], [5, 3]]))

print(Solution().findOrder(
    1, []))
