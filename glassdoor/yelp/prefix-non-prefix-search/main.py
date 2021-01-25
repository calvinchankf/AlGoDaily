from collections import *

"""
    - https://leetcode.com/discuss/interview-question/869337/Yelp-or-Phone-or-Implement-a-prefix-based-search.
    - https://www.1point3acres.com/bbs/thread-541532-1-1.html

    Problem :
    Given a list of business_names (strings) and a searchTerm (string).
    Return a list of business_names that contains searchTerm as prefix in the business_names, case incensitive

    E.g.
    Example
    
    Input:
    business_names = ["Burger King", "Burger King 2", "McDonald's", "super duper burger's", "subway", "pizza hut", "Walburgers"]
    searchTerm = "bur"
    
    Ouput:
    ["Burger King", "Burger King 2", "super duper burger's"]
"""

""" 
    1st: brute force
    Time    O(NC + NW min(C, S))
    Space   O(NC)
"""


def searchBusiness(business_names, searchTerm):
    res = set()
    for i in range(len(business_names)):
        S = business_names[i]
        s = S.lower()
        words = s.split(" ")
        for w in words:
            if w.startswith(searchTerm):
                res.add(S)
    return list(res)


a = ["Burger King", "Burger King 2", "McDonald's",
     "super duper burger's", "subway", "pizza hut", "Walburgers"]
b = "bur"
print(searchBusiness(a, b))

""" 
    2nd: Trie
    Time    O(NC + NWC + S)
    Space   O(NC)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        cur = self.root
        for c in s:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def wordsStartWith(self, s):
        cur = self.root
        for c in s:
            if c not in cur.children:
                return []
            cur = cur.children[c]
        res = []
        q = [(cur, s)]
        while len(q) > 0:
            node, word = q.pop(0)
            if node.isWord:
                res.append(word)
            for c in node.children:
                child = node.children[c]
                q.append((child, word + c))
        return res


def searchBusiness(business_names, searchTerm):
    mapping = defaultdict(set)
    trie = Trie()
    for i in range(len(business_names)):
        S = business_names[i]
        s = S.lower()
        words = s.split(" ")
        for w in words:
            trie.insert(w)
            mapping[w].add(S)

    res = set()
    words = trie.wordsStartWith(searchTerm)
    for w in words:
        res |= mapping[w]
    return list(res)


a = ["Burger King", "Burger King 2", "McDonald's",
     "super duper burger's", "subway", "pizza hut", "Walburgers"]
b = "bur"
print(searchBusiness(a, b))

"""
    Followup: string search

    Input:
    business_names = ["Burger King", "McDonald's", "super duper burger's", "subway", "pizza hut", "Walburgers"]
    searchTerm = "uper bur"
    
    Ouput:
    ["super duper burger's"]

    Brute force
    Time    O(N * min(C, S))

    Or...KMP
"""


def searchBusiness(business_names, searchTerm):
    res = set()
    for i in range(len(business_names)):
        S = business_names[i]
        s = S.lower()
        if searchTerm in s:
            res.add(S)
    return list(res)


a = [
    "Burger King", "Burger King 2", "McDonald's", "super duper burger's", "subway", "pizza hut", "Walburgers"
]
b = "uper bur"
print(searchBusiness(a, b))
