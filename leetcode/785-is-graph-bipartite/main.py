"""
    1st approach: BFS + nodes coloring
    - similar to lc784, 886
    - see .idea.png

    idea learned from others:
    - https://www.youtube.com/watch?v=VlZiMD7Iby4

    Time    O(V+E)
    Space   O(V+E)
    156 ms, faster than 62.09%
"""


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        cache = {}
        for i in range(n):
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
    - see .idea.png

    idea learned from others:
    - https://www.youtube.com/watch?v=VlZiMD7Iby4

    Time    O(V+E)
    Space   O(V+E)
    164 ms, faster than 40.67%
"""


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if self.check(graph, i, 1, seen) == False:
                    return False
        return True

    def check(self, graph, node, color, seen):
        if node in seen:
            if seen[node] != color:
                return False
            return True
        seen[node] = color
        vertices = graph[node]
        for v in vertices:
            if self.check(graph, v, -color, seen) == False:
                return False
        return True
