# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
    questions to ask:
    - negative numbers? yes e.g. "51(-232)(434)"
    - every number is single-digited? no, there might be "51(232)(434)"
    - will the number within 2^32? yes

    this is a followup of leetcode 536)
"""


class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode

        1st approach: recursion
        - get every number by appending digits
        - destruct the ( and ) if any
        - repeat the steps when we encounter a (

        Time    O(n)
        Space   O(h)
        160 ms, faster than 50.32%
        """
        arr = []
        for c in s:
            arr.append(c)
        return self.dfs(arr)

    def dfs(self, arr):
        if len(arr) == 0:
            return None
        
        s = ""
        while len(arr) > 0 and arr[0] != "(" and arr[0] != ")":
            s += arr.pop(0)
        
        num = int(s)
        node = TreeNode(num)
        
        if len(arr) > 0 and arr[0] == "(":
            arr.pop(0)
            node.left = self.dfs(arr)
        if len(arr) > 0 and arr[0] == "(":
            arr.pop(0)
            node.right = self.dfs(arr)
        if len(arr) > 0 and arr[0] == ")":
            arr.pop(0)
        return node


t = Solution().str2tree("4(2(3)(1))(6(5))")
