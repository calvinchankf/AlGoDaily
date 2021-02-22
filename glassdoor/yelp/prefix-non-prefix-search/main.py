from collections import *

"""
    - https://leetcode.com/discuss/interview-question/869337/Yelp-or-Phone-or-Implement-a-prefix-based-search.
    - https://www.1point3acres.com/bbs/thread-541532-1-1.html

    Problem :
    Given a list of business_names (strings) and a searchTerm (string).
    Return a list of business_names that contains searchTerm as prefix in the business_names, case incensitive

    e.g.1
    Input:
    business_names = ["Burger King", "Burger King 2", "McDonald's", "super duper burger's", "subway", "pizza hut", "Walburgers"]
    searchTerm = "bur"
    
    Ouput:
    ["Burger King", "Burger King 2", "super duper burger's"]

    e.g. 2
    Input:
    business_names = ["burger king", "McDonald's", "super duper burger's", "subway", "pizza hut"]
    searchTerm = "duper bur"

    Output:
    ["super duper burger's"]
"""

""" 
    1st: brute force
    Time    O(NC(C + S)) = O(NCC + NCS) N=num of businesses, C=num of characters of every word
    Space   O(NC)
"""


def searchBusiness(business_names, searchTerm):
    res = set()
    for i in range(len(business_names)):
        S = business_names[i]
        s = S.lower()

        # if no "duper bur"
        # words = s.split(" ")
        # for w in words:
        #     if w.startswith(searchTerm):
        #         res.add(S)

        for i in range(len(s)):
            if i == 0 or (s[i-1] == ' ' and s[i] != ' '):
                remain = s[i:]
                if remain.startswith(searchTerm):
                    res.add(S)

    return list(res)


a = ["Burger King", "Burger King 2", "McDonald's",
     "super duper burger's", "subway", "pizza hut", "Walburgers"]
b = "bur"
print(searchBusiness(a, b))

a = ["burger king", "McDonald's", "super duper burger's", "subway", "pizza hut"]
b = "duper bur"
print(searchBusiness(a, b))

print("-----")

""" 
    2nd: Trie
    Time    O(NWCC + NCS) N=num of businesses, W=num of words, C=num of characters of every word
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

        # if no "duper bur"
        # words = s.split(" ")
        # for w in words:
        #     trie.insert(w)
        #     mapping[w].add(S)

        for i in range(len(s)):
            if i == 0 or (s[i-1] == ' ' and s[i] != ' '):
                remain = s[i:]
                trie.insert(remain)
                mapping[remain].add(S)

    res = set()
    words = trie.wordsStartWith(searchTerm)
    for w in words:
        res |= mapping[w]
    return list(res)


a = ["Burger King", "Burger King 2", "McDonald's",
     "super duper burger's", "subway", "pizza hut", "Walburgers"]
b = "bur"
print(searchBusiness(a, b))

a = ["burger king", "McDonald's", "super duper burger's", "subway", "pizza hut"]
b = "duper bur"
print(searchBusiness(a, b))

print("-----")

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


"""

Interviewer: Jackson Breyer, Engineering Manager of the Search UX team
Candidate: Calvin Chan Kin Fung (Full Stack)
Time: 4:00 - 4:45pm PST 

Problem Solving: Bookmark Suggest

Just like a bookmark can save a spot in a book for you, Yelp has a feature 
to save the favorite places you have visited in the past. On mobile devices, 
a user will want to search for one of these businesses, or even search for 
similar businesses as one of these favorites. We will implement a working version of 
this bookmark suggest. 

Part 1

Given a list of bookmark objects and a search term, return bookmarks where the 
search term is a prefix of one of the words in the business name. Return the first 
4 business names that match  the search term. For example: searching for 'bur' in 
these bookmark objects should suggest:
    
    [
        “Burger King” -> ["burger", 'king']
        “Bob's Burgers” -> ['Bob's" , 'Burgers”]
        “Super Duper Burgers” -> ['Super', 'Duper', 'Burgers']
        “Burger King burger” -> ["burger", 'king', ']
    ]
    
    res = [
        burger,
         Bob's Burgers,
        Burger King burger
    ]
    
    - lower cases
    - unique
    - 'Super D' -> []
    - Bob's -> 
"""


def searchBiz(data, searchTerm):
    searchTerm = searchTerm.lower()
    res = []
    for obj in data:
        name = obj['business_name']
        s = name.lower()
        words = s.split()
        for w in words:
            if w.startswith(searchTerm):
                res.append(name)
                break
    return res[:4]


data = [
    {"business_name": "Burger King"},
    {"business_name": "McDonald's"},
    {"business_name": "Bob's Burgers"},
    {"business_name": "Five Guys"},
    {"business_name": "Super Duper Burgers"},
    {"business_name": "Wahlburgers"}
]
searchTerm = 'bur'
print(searchBiz(data, searchTerm))


"""
Part 2

Now we want to also include matches where the search term exists anywhere in the 
business name. We want to give word prefix matches higher priority than non-prefix 
matches. Given the search term 'bur' here is the expected list - note that now 4 
business names are possible:
    - Burger King (prefix match)
    - Bob's Burgers - (prefix match)
    - Super Duper Burgers (prefix match)
    - Wahlburgers (non-prefix match, prefix )
                
    Wahlburgers
     ^
    
    bur = 3
    
    O(N^2)
"""


def searchBiz(data, searchTerm):
    searchTerm = searchTerm.lower()
    prefixRes = []
    nonPrefixRes = []
    for obj in data:
        name = obj['business_name']
        s = name.lower()
        # prefix
        words = s.split()
        isFonud = False
        for w in words:
            if w.startswith(searchTerm):
                prefixRes.append(name)
                if len(prefixRes) == 4:
                    return prefixRes
                isFonud = True
                break
        # non-prefix
        if isFonud:
            continue
        if searchTerm in s:
            nonPrefixRes.append(name)
        if len(prefixRes) + len(nonPrefixRes) == 4:
            return prefixRes + nonPrefixRes

    res = prefixRes + nonPrefixRes
    return res


"""
    prefixRes = [
        Burger King,
        Bob's Burgers,
        Super Duper Burgers,
    ]
    nonPrefixRes = [
        Wahlburgers
    ]
    
    merged = [
        Burger King,
        Bob's Burgers,
        Super Duper Burgers,
        Wahlburgers
    ]
"""

data = [
    {"business_name": "Burger King"},
    {"business_name": "McDonald's"},
    {"business_name": "Bob's Burgers"},
    {"business_name": "Five Guys"},
    {"business_name": "Super Duper Burgers"},
    {"business_name": "Wahlburgers"}
]
searchTerm = 'bur'
print(searchBiz(data, searchTerm))
