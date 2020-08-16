"""
    ref:
    - https://leetcode.com/discuss/interview-question/376375/
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def distanceBetween2ValuesInBST(nums, a, b):
    nums = sorted(nums)
    bst = buildBST(nums, 0, len(nums) - 1)
    lca = lowestCommonAncestor(bst, a, b)
    depthA = findDepth(lca, a)
    depthB = findDepth(lca, b)
    return depthA + depthB


def buildBST(nums, left, right):
    if left > right:
        return None
    mean = (left + right) / 2
    node = TreeNode(nums[mean])
    node.left = buildBST(nums, left, mean - 1)
    node.right = buildBST(nums, mean + 1, right)
    return node


def lowestCommonAncestor(root, p, q):
    curr = root
    left = min(p, q)
    right = max(p, q)
    while True:
        if curr.left != None and right < curr.val:
            curr = curr.left
        elif curr.right != None and left > curr.val:
            curr = curr.right
        else:
            return curr


def findDepth(root, target):
    cur = root
    steps = 0
    while True:
        if cur.val < target:
            cur = cur.right
            steps += 1
        elif cur.val > target:
            cur = cur.left
            steps += 1
        else:
            return steps


print("-----")

print(distanceBetween2ValuesInBST([5, 6, 3, 1, 2, 4], 2, 4))
print(distanceBetween2ValuesInBST([5, 6, 3, 1, 2, 4], 4, 6))
print(distanceBetween2ValuesInBST([5, 6, 3, 1, 2, 4], 4, 5))
