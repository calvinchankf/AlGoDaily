class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


"""
    1st: BFS
    - level order traversal

    Time    O(N)
    Space   O(N)
    52 ms, faster than 81.93%
"""


class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return []
        res = []
        q = [root]
        while len(q) > 0:
            n = len(q)
            arr = []
            for _ in range(n):
                node = q.pop(0)
                arr.append(node.val)
                for child in node.children:
                    q.append(child)
            res.append(arr)
        return res


#       1
#   2   3   4
#  5 6
# 7
a = Node(1, [])
b = Node(2, [])
c = Node(3, [])
d = Node(4, [])
e = Node(5, [])
f = Node(6, [])
g = Node(7, [])

a.children = [b, c, d]
b.children = [e, f]
e.children = [g]

ans = Solution().levelOrder(a)
print("ans=", ans)
