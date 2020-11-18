"""
    ref:
    - https://leetcode.com/discuss/interview-question/376375/
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insertNodeInBst(node, val):
    if node == None:
        return TreeNode(val)
    if val < node.val:
        node.left = insertNodeInBst(node.left, val)
    else:
        node.right = insertNodeInBst(node.right, val)
    return node


def buildBst(nums):
    root = None
    for x in nums:
        root = insertNodeInBst(root, x)
    return root


def lca(node, p, q):
    cur = node
    left = min(p, q)
    right = max(p, q)
    while cur != None:
        if left < cur.val and right < cur.val:
            cur = cur.left
        elif left > cur.val and right > cur.val:
            cur = cur.right
        else:
            return cur
    return cur


def findDepth(root, target):
    cur = root
    steps = 0
    while cur != None:
        if target < cur.val:
            cur = cur.left
            steps += 1
        elif target > cur.val:
            cur = cur.right
            steps += 1
        else:
            return steps
    return -1


"""
    1. build the BST tree
    2. find the common ancestor
    3. the distance between them is the sum of the depth of each the nodes the common ancestor

    Time    O(N)
    Space   O(N)
"""


def bstDistance(values, node1, node2):
    # WRITE YOUR CODE HERE
    bst = buildBst(values)
    ancestor = lca(bst, node1, node2)
    depthA = findDepth(ancestor, node1)
    depthB = findDepth(ancestor, node2)
    if depthA == -1 or depthB == -1:
        return -1
    return depthA + depthB


print("-----")

# 3
print(bstDistance([5, 6, 3, 1, 2, 4], 2, 4))
# -1
print(bstDistance([9, 7, 5, 3, 1], 76, 20))
# 3
print(bstDistance([5, 6, 3, 1, 2, 4], 4, 6))
# 2
print(bstDistance([5, 6, 3, 1, 2, 4], 4, 5))
