"""
    Question:
    - https://leetcode.com/discuss/interview-question/344574/Amazon-or-Phone-Screen-or-Add-new-connection

    Check if an N-ary tree is in valid state after adding a new connection.
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []


def isValid(root, n1, n2):

    hs = set()
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        hs.add(node)
        for child in node.children:
            q.append(child)

    if n1 in hs and n2 in hs:
        return False
    return True
