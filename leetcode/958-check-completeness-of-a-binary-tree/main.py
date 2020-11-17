"""
    2nd approach:
	1. bfs and the queue finally should have all the leafs including null
	2. for a complete binary tree, there should not be any node after we met a null node in the final level

	e.g.1
				1
			2		3
		4 5	 6
	queue = [null, null, null, null, null, null, null]
	parent = 3		4	 4		5	 5		6	 6
	so it is complete

	e.g.2
				1
			2		3
		4 5	 		6
	queue = [null, 6, null, null, null, null]
	parent = 3	   3	4	4	   5	5

	Time	O(n)
	Space	O(h)
	0 ms, faster than 100.00%
"""


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        while q[0] != None:
            node = q.pop(0)
            q.append(node.left)
            q.append(node.right)
        while len(q) > 0 and q[0] == None:
            q.pop(0)
        return len(q) == 0


"""
	2nd approach: level order traversal
	- on a level, there are 2 possible reasons which make the binary tree not complete
		1. there is a null on my left(given that i am a non-null node)
		2. there is a null above my level(given that i am a non-null node)

	Time	O(n)
	Space	O(n)
	32 ms, faster than 21.35%
"""


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        seenNullAbove = False
        while len(q) > 0:
            n = len(q)
            seenNull = False
            for _ in range(n):
                node = q.pop(0)
                if node == None:
                    seenNull = True
                else:
                    if seenNull or seenNullAbove:
                        return False
                    q.append(node.left)
                    q.append(node.right)
            seenNullAbove = seenNull
        return True
