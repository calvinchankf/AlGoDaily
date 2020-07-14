"""
    1st: recursive DFS
    - when we traverse the tree, replace each of a child to its clone using the result from the recursive function

    Time    O(N)
    Space   O(N) recursion tree
    Runtime: 80 ms
    Memory Usage: 17.6 MB
"""


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        node = Node(root.val)
        for child in root.children:
            node.children.append(self.cloneTree(child))
        return node


"""
    2nd: BFS
    - store node and its parent when we traverse the tree
    - append a clone child to its parent every time we dequeue

    Time    O(N)
    Space   O(N) queue
    Runtime: 80 ms, faster than 100.00%
    Memory Usage: 17.6 MB, less than 100.00%
"""


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        newRoot = None
        q = [(None, root)]
        while len(q) > 0:
            parent, head = q.pop(0)
            node = Node(head.val)
            if newRoot == None:
                newRoot = node
            if parent != None:
                parent.children.append(node)
            for child in head.children:
                q.append((node, child))
        return newRoot
