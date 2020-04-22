"""
    1st approach: Binary Segement Tree

    ref:
    https://www.youtube.com/watch?v=rYBtViWXYeI

    Time of build   O(n)
    Time of update  O(logn)
    Time of query   O(logn)
    Space           O(n)
    224ms beats 40.96%
"""


class SNode(object):

    def __init__(self, total, start, end, left, right):
        self.total = total
        self.start = start
        self.end = end
        self.left = left
        self.right = right


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) == 0:
            return
        self.root = self._buildTree(nums, 0, len(nums)-1)

    def _buildTree(self, nums, start, end):
        """
            - divid the array by half
            - build the tree from left and right
            - similar to merge sort
            - the tree that we build is a balanced binary tree
        """
        if start == end:
            return SNode(nums[start], start, end, None, None)
        mid = (start + end)//2
        # from the start to mid
        left = self._buildTree(nums, start, mid)
        # from mid+1 to the end
        right = self._buildTree(nums, mid+1, end)
        return SNode(left.total + right.total, start, end, left, right)

    def _updateTree(self, node, targetIdx, val):
        """
            find the target index by comparing the start and the end
            - if start == end, we reach to the target index
            - if target <= mid, find the left half, else find the right half

            e.g. start -> end = 0 -> 5

            left = (0+5)/2 = 0 -> 2, right = 5-2 = 3 -> 5
        """
        if node.start == targetIdx and node.end == targetIdx:
            node.total = val
            return
        mid = (node.start + node.end)//2
        if targetIdx <= mid:
            self._updateTree(node.left, targetIdx, val)
        else:
            self._updateTree(node.right, targetIdx, val)
        node.total = node.left.total + node.right.total

    def _query(self, node, start, end):
        """
            if the query range is exactly the same of the range of a node, just return the sum/min/max
            , else there are 3 cases:
                - the query range is on your left
                - the query range is on your right
                - part of the query range is on your left, another part is on your right
        """
        if node == None:
            return None
        # if your query exactly fall into the range of a node, just return the sum
        if node.start == start and node.end == end:
            return node.total
        mid = (node.start + node.end)//2
        if end <= mid:
            # if the end of your qeury <= mid point, search left hand side
            # remember that we divide our range like this 0->5 = (0+5)/2 = 0->2, 3->5
            # so use end <= mid but not end < mid
            return self._query(node.left, start, end)
        elif start > mid:
            # if the start of your qeury > mid point, search right hand side
            return self._query(node.right, start, end)
        else:
            # if unfortunately the query range is just partially covered
            return self._query(node.left, start, mid) + self._query(node.right, mid+1, end)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self._updateTree(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._query(self.root, i, j)


"""
    2nd approach: Binary Indexed Tree(Fenwick Tree)

    ref:
    - https://www.youtube.com/playlist?list=PLDV1Zeh2NRsCvoyP-bztk6uXAYoyZg_U9
    - https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation
    - https://www.youtube.com/watch?v=uSFzHCZ4E-8

    2's complement binary representation for negative numbers
    - youtube.com/watch?v=4qH4unVtJkE&vl=en

    Time of build   O(n)
    Time of update  O(logn)
    Time of query   O(logn)
    Space           O(n)
    224ms beats 40.96%
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.fenwickTree = (len(nums)+1) * [0]

        for i in range(len(nums)):
            self._buildTree(i, nums[i])

    def _buildTree(self, i, val):
        k = i + 1
        # new i = i + least significant bit(i)
        # e.g. start from 5
        # 5     00101
        # 6     00110 (becos 00101 + 00001)
        # 8     01000 (becos 00110 + 00010)
        # 16    10000 (becos 01000 + 01000)
        while k < len(self.fenwickTree):
            self.fenwickTree[k] += val
            k = k + (k & -k)

    def _getSum(self, i):
        s = 0
        k = i + 1
        # flip the least significant bit 1 by 1 to the left until 0
        # e.g. start from 14
        # 14    1110
        # 12    1100 (1110 - 0010)
        # 8     1000 (1100 - 0100)
        # 0     0000 (1000 - 1000)
        while k > 0:
            s += self.fenwickTree[k]
            k = k - (k & -k)
        return s

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self._buildTree(i, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._getSum(j) - self._getSum(i-1)
