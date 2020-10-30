# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
    1st: recursion
    - inorder traversal the tree and put the values into an array
    - maintain an index to indicate the current item we visit

    Time    O(N)
    Space   O(N)
    504 ms, faster than 100.00%
"""


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.arr = []
        self._inorder(root)
        self.curIdx = -1

    def _inorder(self, node):
        if node == None:
            return
        self._inorder(node.left)
        self.arr.append(node.val)
        self._inorder(node.right)

    def hasNext(self) -> bool:
        return self.curIdx + 1 < len(self.arr)

    def next(self) -> int:
        self.curIdx += 1
        return self.arr[self.curIdx]

    def hasPrev(self) -> bool:
        return self.curIdx - 1 >= 0

    def prev(self) -> int:
        self.curIdx -= 1
        return self.arr[self.curIdx]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()
