"""
    1st approach: BFS + nodes coloring
    - similar to lc784, 886

    idea learned from others:
    - https://www.youtube.com/watch?v=VlZiMD7Iby4

    Time    O(V+E)
    Space   O(V+E)
    812 ms, faster than 22.78%
"""


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = {}
        for i in range(1, N+1):
            graph[i] = []

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        # n = len(graph)
        cache = {}
        for i in range(1, N+1):
            if i not in cache:
                if self.bfs(graph, i, cache) == False:
                    return False
        return True

    def bfs(self, graph, start, cache):
        q = [(start, 1)]
        while len(q) > 0:
            node, color = q.pop(0)
            if node in cache:
                if cache[node] != color:
                    return False
                continue
            cache[node] = color
            for nb in graph[node]:
                q.append((nb, -color))
        return True


"""
    2nd approach: recursive DFS + nodes coloring

    idea learned from others:
    - https://www.youtube.com/watch?v=VlZiMD7Iby4

    Time    O(V+E)
    Space   O(V+E)
    660 ms, faster than 53.79%
"""


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        connections = []
        for _ in range(N+1):
            connections.append([])

        for a, b in dislikes:
            connections[a].append(b)
            connections[b].append(a)

        seen = {}
        for i in range(len(connections)):
            if i not in seen:
                if self.check(connections, i, 1, seen) == False:
                    return False
        return True

    def check(self, connections, node, color, seen):
        if node in seen:
            if seen[node] != color:
                return False
            return True
        seen[node] = color
        vertices = connections[node]
        for v in vertices:
            if self.check(connections, v, -color, seen) == False:
                return False
        return True
