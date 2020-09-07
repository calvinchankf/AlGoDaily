"""
    https://leetcode.com/discuss/interview-question/782606/

    Find the largest group of associated items. If there is a tie, return the group that first appears in lexicographical order
    Input: edges between the items
    Output: a list of associated items

    e.g.1
    edges= [
        ['a', 'b'],
        ['c', 'd'],
        ['d', 'e'],
    ]
    output: ['c', 'd', 'e']
    explanation: there are 2 groups: ['a','b'] and ['c', 'd', 'e']. Clearly, the secound group is larger

    e.g.2
    edges = [
        ['d', 'e'],
        ['e', 'f'],
        ['a', 'b'],
        ['b', 'c']
    ]
    output: ['a', 'b', 'c']
    explanation: there are 2 groups: [d', 'e', 'f'] and ['a','b'','c]. They have the same size but the second group is lexicographically smaller
"""


class UnionFind(object):
    def __init__(self, vertices):
        self.roots = {}
        self.caps = {}
        for vertex in vertices:
            self.roots[vertex] = vertex
            self.caps[vertex] = 1

    def find(self, key):
        if key not in self.roots:
            return None
        # loop to find to ultimate root
        cur = key
        while cur != self.roots[cur]:
            cur = self.roots[cur]
        return cur

    def union(self, p, q):
        if p not in self.roots or q not in self.roots:
            return
        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.roots[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.roots[qId] = pId
            self.caps[pId] += self.caps[qId]


class Solution(object):

    def largestItemAssociation(self, pairs):
        itemSet = set()
        for a, b in pairs:
            itemSet.add(a)
            itemSet.add(b)
        items = list(itemSet)

        # union the pairs
        uf = UnionFind(items)
        for a, b in pairs:
            uf.union(a, b)

        # find the root of each item
        ht = {}
        for item in items:
            root = uf.find(item)
            if root in ht:
                ht[root].append(item)
            else:
                ht[root] = [item]

        # find the largest group
        largestGroup = []
        for key in ht:
            if len(ht[key]) > len(largestGroup):
                largestGroup = ht[key]
            elif len(ht[key]) == len(largestGroup):
                lexiA = ','.join(ht[key])
                lexiB = ','.join(largestGroup)
                if lexiA < lexiB:
                    largestGroup = ht[key]

        return sorted(largestGroup)


s = Solution()

# a,b | c,d,e
a = [
    ['a', 'b'],
    ['c', 'd'],
    ['d', 'e'],
]
print(s.largestItemAssociation(a))

# 1,2,5 | 3,4
a = [
    ['item1', 'item2'],
    ['item2', 'item5'],
    ['item3', 'item4']
]
print(s.largestItemAssociation(a))

# 1,2,3 | 4,5,6
a = [
    ['item4', 'item5'],
    ['item5', 'item6'],
    ['item1', 'item2'],
    ['item2', 'item3']
]
print(s.largestItemAssociation(a))
