from collections import Counter

"""
    You are given a tree that contains N nodes, each containing an integer u which corresponds to a lowercase character c in the string s using 1-based indexing.
    You are required to answer Q queries of type [u, c], where u is an integer and c is a lowercase letter. The query result is the number of nodes in the subtree of node u containing c.
    
    Signature
    int[] countOfNodes(Node root, ArrayList<Query> queries, String s)
    
    Input
    A pointer to the root node, an array list containing Q queries of type [u, c], and a string s
    
    Constraints
    N and Q are the integers between 1 and 1,000,000
    u is a unique integer between 1 and N
    s is of the length of N, containing only lowercase letters
    c is a lowercase letter contained in string s
    Node 1 is the root of the tree
    
    Output
    An integer array containing the response to each query
    
    Example
            1(a)
            /   \
          2(b)  3(a)
    s = "aba"
    RootNode = 1
    query = [[1, 'a']]
    
    Note: Node 1 corresponds to first letter 'a', Node 2 corresponds to second letter of the string 'b', Node 3 corresponds to third letter of the string 'a'.
    output = [2]
    
    Both Node 1 and Node 3 contain 'a', so the number of nodes within the subtree of Node 1 containing 'a' is 2.
    --------------------------------------------------------------------------------
    s means the character at every node val(1 based)

    0123456
    abaacab
"""


class Node:
    def __init__(self, data):
        self.val = data
        self.children = []


def count_of_nodes(root, queries, s):
    ht = {}

    def count(node):
        _ht = Counter()
        _ht[s[node.val-1]] = 1

        for child in node.children:
            _ht += count(child)

        ht[node.val] = _ht
        return _ht
    count(root)

    res = []
    for u, c in queries:
        if u in ht and c in ht[u]:
            res.append(ht[u][c])
        else:
            res.append(0)
    return res


# [2]
n_1, q_1 = 3, 1
s_1 = "aba"
root_1 = Node(1)
root_1.children.append(Node(2))
root_1.children.append(Node(3))
queries_1 = [(1, 'a')]
r = count_of_nodes(root_1, queries_1, s_1)
print(r)

# [4, 1, 2]
n_2, q_2 = 7, 3
s_2 = "abaacab"
root_2 = Node(1)
root_2.children.append(Node(2))
root_2.children.append(Node(3))
root_2.children.append(Node(7))
root_2.children[0].children.append(Node(4))
root_2.children[0].children.append(Node(5))
root_2.children[1].children.append(Node(6))
queries_2 = [(1, 'a'), (2, 'b'), (3, 'a')]
r = count_of_nodes(root_2, queries_2, s_2)
print(r)
