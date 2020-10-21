# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    exactly as lc297

    easy approach: similar to lc536, 572, 606
    e.g. 1(2()())(3(4()())(5()()))

    Time    O(n)
    Space   O(h)
    656 ms, faster than 5.27%
"""
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root == None:
            return ''
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + '(' + left + ')(' + right + ')'
        

    def deserialize(self, s: str) -> TreeNode:
        """Decodes your encoded data to tree.
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

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans