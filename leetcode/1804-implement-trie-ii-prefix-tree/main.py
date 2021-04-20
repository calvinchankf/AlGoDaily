"""
    1st: trie
    - similar to lc208
    - BFS to count the nodes which start with prefix
    
    Time    O(N)
    Space   O(N)
    1616 ms, faster than 100.00%
"""
class Node(object):
    def __init__(self, count=0):
        self.children = 26 * [None]
        self.count = count


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Node()
            cur = cur.children[idx]
        cur.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.children[idx] == None:
                return 0
            cur = cur.children[idx]
        return cur.count

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for w in prefix:
            idx = ord(w) - ord('a')
            if cur.children[idx] == None:
                return 0
            cur = cur.children[idx]

        res = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        q = [(cur, '')]
        while len(q) > 0:
            node, path = q.pop(0)
            if node == None:
                continue
            res += node.count
            for i in range(len(node.children)):
                child = node.children[i]
                q.append((child, path + alphabet[i]))
        return res

    def erase(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.children[idx] == None:
                return
            cur = cur.children[idx]
        if cur.count > 0:
            cur.count -= 1