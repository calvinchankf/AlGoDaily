"""
    1st: trie
    
    Time    O(N)
    Space   O(N)
    108 ms, faster than 91.26%
"""


class Node(object):
    def __init__(self, is_word):
        self.children = 26*[None]
        self.is_word = is_word


class Trie(object):

    def __init__(self):
        self.root = Node(False)

    def insert(self, word):
        cur = self.root
        for c in word:
            idx = ord(c)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur = cur.children[idx]
        cur.is_word = True

    def search(self, word):
        s = ''
        cur = self.root
        for c in word:
            if cur.is_word:
                return s
            idx = ord(c)-ord('a')
            if cur.children[idx] == None:
                return None
            cur = cur.children[idx]
            s += c
        return s if cur.is_word else None


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        for w in dictionary:
            trie.insert(w)
        res = ''
        words = sentence.split()
        for w in words:
            b = trie.search(w)
            if b != None:
                res += b + ' '
            else:
                res += w + ' '
        return res[:-1]
