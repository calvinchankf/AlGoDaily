class Node(object):
    def __init__(self, is_word):
        self.children = 26*[None]
        self.is_word = is_word


class Trie(object):

    def __init__(self):
        self.root = Node(False)

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
            cur = cur.children[idx]
        cur.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for w in word:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        return cur.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for w in prefix:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        return True

    def startsWith(self, prefix):
        """
        followup: print all the words startwith prefix

        Returns '' if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: []
        """
        cur = self.root
        for w in prefix:
            idx = ord(w)-ord('a')
            if cur.children[idx] == None:
                return []
            cur = cur.children[idx]

        res = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        def dfs(node, path):
            if node == None:
                return
            if node.is_word:
                res.append(prefix+path)
            for i in range(len(node.children)):
                child = node.children[i]
                dfs(child, path + alphabet[i])

        dfs(cur, "")
        return res


obj = Trie()
obj.insert('abc')
obj.insert('calvin')
obj.insert('callon')
obj.insert('car')
obj.insert('ce')
# print(obj.root.children)
print(obj.search('abc'))
print(obj.startsWith('c'))
print(obj.startsWith('ca'))
print(obj.startsWith('cal'))
