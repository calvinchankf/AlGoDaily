"""
    1st: brute force

    Time    O(N^3)
    Space   O(N)
    LTE
"""


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i+1] = set()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        res = 2**31
        seen = set()
        for i in range(1, n+1):
            if len(graph[i]) < 2:
                continue
            cands = list(graph[i])
            _n = len(cands)
            for j in range(_n):
                for k in range(j+1, _n):
                    left = cands[j]
                    right = cands[k]
                    if left in graph[right] and right in graph[left]:
                        trio = sorted([i, left, right])
                        key = tuple(trio)
                        if key in seen:
                            continue
                        seen.add(key)
                        # print(trio)
                        score = 0
                        for node in trio:
                            score += len(graph[node])
                        res = min(res, score - 6)
        if res == 2**31:
            return -1
        return res


"""
    2nd: optimize 1st with 'Adjacency Matrix'
    - https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/discuss/1064557/C%2B%2B-O(n-3)-Adjacency-List-vs.-Matrix
    - https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/discuss/1067012/JavaC%2B%2B-Brute-Force-Solution-Works-Here

    Time    O(N^3) the worst
    Space   O(N)
    5684 ms, faster than 72.99%
"""


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        isConnected = []
        indegrees = []
        for i in range(n):
            indegrees.append(0)
            isConnected.append(n * [False])
        for _u, _v in edges:
            u = _u - 1
            v = _v - 1
            isConnected[u][v] = True
            isConnected[v][u] = True
            indegrees[u] += 1
            indegrees[v] += 1
        res = 2**32
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if isConnected[i][j] and isConnected[j][k] and isConnected[k][i]:
                        res = min(res, indegrees[i] +
                                  indegrees[j] + indegrees[k] - 6)
        if res == 2**32:
            return -1
        return res
