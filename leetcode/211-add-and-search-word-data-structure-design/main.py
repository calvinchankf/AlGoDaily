"""
    1st: trie + dfs

    Time of search      O(26^C)
    Space               O(N)
    468 ms, faster than 32.13%
"""


class Node(object):
    def __init__(self, isWord=False):
        self.children = 26 * [None]
        self.isWord = isWord


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            key = ord(c) - ord('a')
            if cur.children[key] == None:
                cur.children[key] = Node()
            cur = cur.children[key]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(remain, node):
            if node == None:
                return False
            if len(remain) == 0:
                return node.isWord

            firstChar = remain[0]
            nextRemain = remain[1:]

            if firstChar == '.':
                for i in range(26):
                    if dfs(nextRemain, node.children[i]):
                        return True
                return False

            key = ord(firstChar) - ord('a')
            nextNode = node.children[key]
            return dfs(nextRemain, nextNode)

        return dfs(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
