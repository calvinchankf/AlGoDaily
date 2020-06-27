"""
    1st approach: BFS + nodes coloring
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
        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if self.check(graph, i, seen) == False:
                    return False
        return True

    def check(self, graph, start, seen):
        q = [(start, 1)]
        while len(q) > 0:
            pop, color = q.pop(0)
            if pop in seen:
                if seen[pop] != color:
                    return False
                continue
            seen[pop] = color
            vertices = graph[pop]
            for v in vertices:
                q.append((v, -color))
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
