"""
    approach: trie
    - nothing special but the descrition is ambiguous

    e.g. `If it is a file path, return a list that only contains this file's name`
    - it means `return the target file only`

    Time of insert()        O(N)    N: number of folder in the path
    Time of searchFile()    O(N)
    Time of startWith()     O(N)
    Space                   O(A)    A: all folders
    40 ms, faster than 96.88%
"""


class Node(object):
    def __init__(self):
        self.children = {}
        self.fileContent = ''
        self.isDir = True


class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, path):
        cur = self.root
        folders = path[1:].split('/')
        for f in folders:
            if f not in cur.children:
                cur.children[f] = Node()
            cur = cur.children[f]
        return cur

    def searchFile(self, path):
        cur = self.root
        folders = path[1:].split('/')
        for f in folders:
            if f not in cur.children:
                return ''
            cur = cur.children[f]
        return cur

    def startWith(self, path):
        if path == '/':
            return [key for key in self.root.children]
        cur = self.root
        folders = path[1:].split('/')
        for f in folders:
            if f not in cur.children:
                return []
            cur = cur.children[f]
        if cur.isDir:
            return [key for key in cur.children]
        return [f]
        # # return all files/folders that share the same prefix
        # siblings = []
        # for key in children:
        #     if key.startswith(f):
        #         siblings.append(key)
        # return siblings


class FileSystem(object):

    def __init__(self):
        self.trie = Trie()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        res = self.trie.startWith(path)
        return sorted(res)

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        self.trie.insert(path)

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        node = self.trie.insert(filePath)
        node.isDir = False
        node.fileContent += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        f = self.trie.searchFile(filePath)
        return f.fileContent


fs = FileSystem()
fs.mkdir('/goowmfn')
print(fs.ls('/goowmfn'))
print(fs.ls('/'))
fs.mkdir('/z')
print(fs.ls('/'))
print(fs.ls('/'))
fs.addContentToFile('/goowmfn/c', "shetopcy")
print(fs.ls('/z'))
print(fs.ls('/goowmfn/c'))
print(fs.ls('/goowmfn'))

print("-----")
