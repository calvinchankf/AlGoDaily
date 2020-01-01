from collections import defaultdict

"""
    1st: union find + recursion

    Time    O(2N + NlogN + k!) k=number of words which have sysnonym
    Space   O(3N + k!)
    20 ms, faster than 53.37%
"""


class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        hs = set()
        for a, b in synonyms:
            hs.add(a)
            hs.add(b)
        uf = UnionFind(hs)
        for a, b in synonyms:
            uf.union(a, b)

        rawWords = text.split()
        words = []
        for word in rawWords:
            root = uf.find(word)
            if root == None:
                words.append(word)
            else:
                words.append(root)

        self.ht = defaultdict(list)
        for word in hs:
            root = uf.find(word)
            if root != None:
                self.ht[root].append(word)
        for key in self.ht:
            self.ht[key] = sorted(self.ht[key])

        self.res = []
        self.dfs(words, '')
        return self.res

    def dfs(self, words, s):
        if len(words) == 0:
            self.res.append(s[1:])
            return
        word = words[0]
        if word in self.ht:
            for synonym in self.ht[word]:
                self.dfs(words[1:], s + ' ' + synonym)
        else:
            self.dfs(words[1:], s + ' ' + word)


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.ids = {}
        self.caps = {}
        for vertex in vertices:
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def find(self, key):
        if key not in self.ids:
            return None
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
