from collections import Counter

# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

"""
    1st: hashtable + linked list traversal

    Time    O(M+N)
    Space   O(M+N)
    484 ms, faster than 100.00%
"""

class Solution:
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        ht = Counter()
        cur = poly1
        while cur != None:
            ht[cur.power] = cur.coefficient
            cur = cur.next
        cur = poly2
        while cur != None:
            ht[cur.power] += cur.coefficient
            cur = cur.next
        
        sortedMap = []
        for power in ht:
            sortedMap.append((power, ht[power]))
        sortedMap.sort(reverse=True)
        
        dumphead = PolyNode()
        cur = dumphead
        for power, coeff in sortedMap:
            if coeff != 0:
                cur.next = PolyNode(coeff, power)
                cur = cur.next
        return dumphead.next