"""
    Given an array of words, find all shortest unique prefixes to represent each word in the given array. 
    Assume that no word is prefix of another.
"""


class Node(object):
    def __init__(self, freq=0):
        self.children = 26*[None]
        self.freq = freq


class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node(False)
            cur.freq += 1
            cur = cur.children[idx]
        cur.freq += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        prefix = ''
        for w in word:
            idx = ord(w)-ord('a')
            cur = cur.children[idx]
            prefix += w
            if cur.freq == 1:
                return prefix
        return prefix


def shortestUniquePrefix(arr):
    trie = Trie()
    for w in arr:
        trie.insert(w)
    # print(trie.root.freq) # total number of items in the trie
    res = []
    for w in arr:
        temp = trie.search(w)
        res.append(temp)
    return res


a = ["zebra", "dog", "duck", "dove", "calvin", "car", "alphago", "alphabet"]
print(shortestUniquePrefix(a))
