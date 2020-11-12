from collections import defaultdict
"""
    https://leetcode.com/discuss/interview-question/903941/Facebook-or-Phone-or-Accounts-Merge

    Location: Menlo Park
    Position: Intern

    This is a question that I got on a FB intern phone screen that stumped me. 
    The input is basically a list of these emails linked to an ID, 
    and you need to give the output with IDs that are associated with one individual as shown. 
    
    Anyone have an idea of how to go about solving this? Thanks!

    Input:
    C1: bob@yahoo.com, bob@gmail.com
    C2: mary@facebook.com
    C3: bob@gmail.com, bob_1@hotmail.com, bob@facebook.com
    C4: bob_1@hotmail.com
    C5: mary@facebook.com
    C6: mark@gmail.com

    Output: [[C1, C3, C4], [C2, C5], [C6]]
"""


def accountsMerge(idAndEmails):
    ht = defaultdict(set)
    for uid in idAndEmails:
        emails = idAndEmails[uid]
        for e in emails:
            ht[e].add(uid)
    # union
    uf = UnionFind(idAndEmails)
    for key in ht:
        uids = list(ht[key])
        a = uids[0]
        for i in range(1, len(uids)):
            b = uids[i]
            uf.union(a, b)
    # group uids
    resultSet = defaultdict(list)
    for uid in idAndEmails:
        root = uf.find(uid)
        resultSet[root].append(uid)
    # construct the result
    res = []
    for key in resultSet:
        res.append(resultSet[key])
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


a = {
    'C1': ['bob@yahoo.com', 'bob@gmail.com'],
    'C2': ['mary@facebook.com'],
    'C3': ['bob@gmail.com', 'bob_1@hotmail.com', 'bob@facebook.com'],
    'C4': ['bob_1@hotmail.com'],
    'C5': ['mary@facebook.com'],
    'C6': ['mark@gmail.com'],
}
print(accountsMerge(a))
