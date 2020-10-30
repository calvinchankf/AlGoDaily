import json
# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    easy approach: similar to lc536, 572, 606
    e.g. 1(2()())(3(4()())(5()()))

    Time    O(n)
    Space   O(h)
    476 ms, faster than 5.11% <= string will be very long due to the redundant empty nodes '()' 
"""


class Codec:

    def serialize(self, node):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if node == None:
            return ''
        left = self.serialize(node.left)
        right = self.serialize(node.right)
        return str(node.val) + '(' + left + ')(' + right + ')'
        

    def deserialize(self, s):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(s) == 0:
            return None
        arr = []
        # execpt the open and end parentheses
        for c in s:
            arr.append(c)
        return self.deserializeHelper(arr)
    
    def deserializeHelper(self, arr):
        if len(arr) == 0:
            return None
                
        s = ""
        while len(arr) > 0 and arr[0] != "(" and arr[0] != ")":
            s += arr.pop(0)
        
        node = None
        if len(s) > 0:
            num = int(s)
            node = TreeNode(num)

        # left child
        if len(arr) > 0 and arr[0] == "(":
            arr.pop(0)
            node.left = self.deserializeHelper(arr)

        # right child
        if len(arr) > 0 and arr[0] == "(":
            arr.pop(0)
            node.right = self.deserializeHelper(arr)

        # end this scope
        if len(arr) > 0 and arr[0] == ")":
            arr.pop(0)
        return node


"""
    my 1st approach
    bfs, iterative
    it is what leetcode does, e.g. [1,2,3,null,null,4,5]

    Time    O(n)
    Space   O(h)
    132 ms beats 48%
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            for i in range(len(queue)):
                head = queue.pop(0)
                if head != None:
                    result.append(head.val)
                    if head.left != None:
                        queue.append(head.left)
                    else:
                        queue.append(None)
                    if head.right != None:
                        queue.append(head.right)
                    else:
                        queue.append(None)
                else:
                    result.append(None)
        # remove tailing nulls
        for i in range(len(result)):
            idx = len(result) - 1
            if result[idx] is None:
                result.pop()
        # to string
        temp = ','.join(str(e) if e is not None else 'null' for e in result)
        return '['+temp+']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = json.loads(data)
        if len(arr) == 0:
            return None
        root = TreeNode(arr[0])
        queue = []
        queue.append(root)
        i = 1
        while len(queue) > 0:
            n = len(queue)
            for j in range(n):
                head = queue.pop(0)
                if i+2*j < len(arr) and arr[i+2*j] is not None:
                    left = TreeNode(arr[i+2*j])
                    head.left = left
                    queue.append(left)
                if i+2*j+1 < len(arr) and arr[i+2*j+1] is not None:
                    right = TreeNode(arr[i+2*j+1])
                    head.right = right
                    queue.append(right)
            i += 2*n
        return root


"""
    suggested approach
    dfs, recursive, e.g. 1,2,null,null,3,4,null,null,5,null,null,
"""


class Codec1:

    def serialize(self, root):
        result = []

        def helper(node):
            if node is None:
                result.append('null')
            else:
                result.append(str(node.val))
                helper(node.left)
                helper(node.right)
            return

        helper(root)
        return ','.join(result)

    def deserialize(self, data):
        def helper(arr):
            if arr[0] == 'null':
                arr.pop(0)
                return None
            node = TreeNode(arr.pop(0))
            node.left = helper(arr)
            node.right = helper(arr)
            return node

        temp = data.split(',')
        root = helper(temp)
        return root


# for checking
def test_level_order(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    result = []
    if not root:
        return result
    queue = []
    queue.append(root)
    while len(queue) > 0:
        level = []
        level_node_count = len(queue)
        for idx in range(0, level_node_count):
            node = queue.pop(0)
            level.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        result.append(level)
    print(result)
    return result


#       1
#    2      3
#         4   5
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e

# test bfs
codec = Codec()
serial = codec.serialize(a)
print(serial)
node = codec.deserialize(serial)
test_level_order(node)

# test dfs
codec = Codec1()
serial = codec.serialize(a)
print(serial)
node = codec.deserialize(serial)
test_level_order(node)
