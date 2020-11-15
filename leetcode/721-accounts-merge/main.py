from collections import defaultdict

"""
    1st: union find
    - get all the emails
    - map each email with a name
    - union find all the emails using the input
    - iterate the input again: map each of the email to its corresponding root

    Time    O(nlogn)
    Space   O(n)
    228 ms, faster than 40.59% 
"""


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        emails = {}
        for row in accounts:
            username = row[0]
            for i in range(1, len(row)):
                email = row[i]
                emails[email] = username
        # union
        uf = UnionFind(emails)
        for row in accounts:
            a = row[1]
            for i in range(2, len(row)):
                b = row[i]
                uf.union(a, b)
        # group the emails
        resultSet = defaultdict(list)
        for e in emails:
            root = uf.find(e)
            resultSet[root].append(e)
        # construct the result
        res = []
        for rootEmail in resultSet:
            username = emails[rootEmail]
            row = [username] + sorted(resultSet[rootEmail])
            res.append(row)
        return res


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.ids = {}
        self.caps = {}
        for vertex in vertices:
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def find(self, key):
        # loop to find to ultimate root
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
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


s = Solution()
r = s.accountsMerge([
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"]
])
print(r)
