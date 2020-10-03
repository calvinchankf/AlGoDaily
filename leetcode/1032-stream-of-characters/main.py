from collections import defaultdict

"""
    1st: suffix trie
    
    Time of __init__()      O(W)
    Space of query()        O(N)
    1300 ms, faster than 37.44%
"""


class Node(object):
    def __init__(self, isWord=False):
        self.children = 26*[None]
        self.isWord = isWord


class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node()
            cur = cur.children[idx]
        cur.isWord = True

    def search(self, word):
        cur = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
            if cur.isWord:
                return True
        return False


class StreamChecker(object):

    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.cur = ''

    def query(self, letter):
        self.cur = letter + self.cur
        return self.trie.search(self.cur)


"""
    2nd: hashtable
    - init(words): put the words into a hashtable with the last character as key
        e.g, words = [a, bc, def, ok, lok, ook]
        hashtable = {
            a: a,
            c: bc,
            f: def,
            k: ok, lok, ook
        }
    - query(letter): for each set of key(letter), i.e, hashtabe[letter], check if the aggregated string exists
        e.g. abcdfgdlo[k]   <- k is the latest query
        hashtable[k] = {ok, lok, ook}
        Since aggregated string ends with ok, lok, return True
"""


class StreamChecker:

    def __init__(self, words):
        self.s = ''
        self.ht = defaultdict(set)
        for w in words:
            self.ht[w[-1]].add(w)

    def query(self, letter):
        self.s += letter
        # approach 1: 4 lines
        res = False
        for w in self.ht[letter]:
            res = res or self.s.endswith(w)
        return res
        # approach 2: Or 1 line
        # return any(self.s.endswith(w) for w in self.dic[letter])
