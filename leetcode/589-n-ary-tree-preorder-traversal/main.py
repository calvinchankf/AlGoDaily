class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


# iterative: stack
"""
    1st: stack

    Time    O(N)
    Space   O(N)
    52 ms, faster than 57.84%
"""


class Solution(object):
    def preorder(self, root):
        if root == None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node.val != None:
                res.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return res


"""
    2nd: recursion

    Time    O(N)
    Space   O(H)
    44 ms, faster than 93.90%
"""


class Solution(object):
    def preorder(self, root):
        res = []

        def f(node):
            if node == None:
                return
            res.append(node.val)
            for child in node.children:
                f(child)

        f(root)
        return res
