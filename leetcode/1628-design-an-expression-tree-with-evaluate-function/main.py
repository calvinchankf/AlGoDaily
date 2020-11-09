import abc 
from abc import ABCMeta, abstractmethod 

"""
    1st: recursion
    - queue + recursion to buildTree()
    - recursion to evaluate()

    Time of buildTree()     O(N)
    Time of evaluate()      O(N)
    Space                   O(N)
    20 ms, faster than 100.00%
"""


"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node:
    __metaclass__ = ABCMeta
    # define your fields here
    @abstractmethod
    def evaluate(self):
        pass
        
class TreeNode(Node):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def evaluate(self):
        if self == None:
            return 0
        x = self.val
        if x.isdigit():
            return int(x)
        left = self.left.evaluate()
        right = self.right.evaluate()
        if x == '+':
            return left + right
        elif x == '-':
            return left - right
        elif x == '*':
            return left * right
        elif x == '/':
            return left // right


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix):
        """
        :type s: List[str]
        :rtype: int
        """
        val = postfix.pop()
        node = TreeNode(val)
        if val.isdigit():
            return node
        node.right = self.buildTree(postfix)
        node.left = self.buildTree(postfix)
        return node
        

"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        