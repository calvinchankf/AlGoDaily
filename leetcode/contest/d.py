from collections import defaultdict


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.collections = defaultdict(list)
        self.ht = {}

        for i in range(len(parent)):
            parentNode = parent[i]
            self.collections[parentNode].append(i)

        self.dfs(0, [])

    def getKthAncestor(self, node: int, k: int) -> int:
        arr = self.ht[node]
        i = len(arr) - k - 1
        if i >= 0:
            return arr[i]
        return -1

    def dfs(self, node, path):

        path_ = path[:] + [node]

        self.ht[node] = path_

        for child in self.collections[node]:
            self.dfs(child, path_)


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.collections = defaultdict(list)
        self.ht = {}

        for i in range(len(parent)):
            parentNode = parent[i]
            self.collections[parentNode].append(i)

        self.dfs(0, 'x')

    def getKthAncestor(self, node: int, k: int) -> int:
        s = self.ht[node]
        arr = s.split(',')
        arr.pop(0)
        i = len(arr) - k - 1
        if i >= 0:
            return arr[i]
        return -1

    def dfs(self, node, path):

        path_ = path + ',' + str(node)

        self.ht[node] = path_

        for child in self.collections[node]:
            self.dfs(child, path_)
