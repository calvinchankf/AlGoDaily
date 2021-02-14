"""
    1st approach: union find
    - put the friends connections into an union find
    - return the total 'cluster' as a result

    Time		O(NNlogN) -> O(N^3)
    Space		O(N)
    204 ms, faster than 24.89
"""


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        uf = UnionFind(N)
        for i in range(N):
            for j in range(i+1, N):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.count


class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.ids = {}
        self.caps = {}
        for i in range(n):
            self.ids[i] = i
            self.caps[i] = 1

    def find(self, key):
        # loop to find to ultimate root
        if key not in self.ids:
            return None
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        if p not in self.ids or q not in self.ids:
            return

        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1


"""
    2nd approach: bfs
    - get the friend list for each friend
    - for each person, bfs to find all of his friends and put them into history
    - after finished one bfs, it means that we are done with one 'cluster'

    Time		O(NN)
    Space		O(N)
    220 ms, faster than 23.64%
"""


class Solution(object):
    def findCircleNum(self, M):
        n = len(M)
        graph = defaultdict(set)
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)
        res = 0
        seen = set()
        for i in range(n):
            if i in seen:
                continue
            self.bfs(graph, i, seen)
            res += 1
        return res

    def bfs(self, graph, start, seen):
        q = [start]
        while len(q) > 0:
            node = q.pop(0)
            if node in seen:
                continue
            seen.add(node)
            if node not in graph:
                continue
            for nb in graph[node]:
                q.append(nb)


a = [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]]
print(Solution().findCircleNum(a))

a = [[1, 1, 0],
     [1, 1, 0],
     [0, 0, 1]]
print(Solution().findCircleNum(a))

a = [[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0], [0, 1, 0, 1]]
print(Solution().findCircleNum(a))
