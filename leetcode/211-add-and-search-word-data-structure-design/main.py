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
            return dfs(nextRemain, node.children[key])

        return dfs(word, self.root)


print("-----")


"""
    2nd: trie + bfs

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
        self.trie = Node()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] == None:
                cur.children[i] = Node()
            cur = cur.children[i]
        cur.isWord = True

    def search(self, word: str) -> bool:
        q = [(word, self.trie)]
        while len(q) > 0:
            s, cur = q.pop(0)
            if cur == None:
                continue
            if len(s) == 0:
                if cur.isWord:
                    return True
                continue
            c = s[0]
            remain = s[1:]
            if c == '.':
                for i in range(26):
                    q.append((remain, cur.children[i]))
            else:
                i = ord(c) - ord('a')
                q.append((remain, cur.children[i]))
        return False
