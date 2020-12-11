
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    1st: linked list
    - find the places to remove
    - insert the lists in between

    Time    O(M+N)
    Space   O(1)
    504 ms, faster than 50.00%
"""


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dumphead = ListNode()
        dumphead.next = list1
        cur = list1
        nodeA = None
        nodeB = None
        while cur != None:
            if cur.next != None and cur.next.val == a:
                nodeA = cur
            if cur.val == b:
                nodeB = cur.next
            cur = cur.next
        cur = list1
        while cur != None:
            if cur == nodeA:
                cur.next = list2
            if cur.next == None:
                cur.next = nodeB
                break
            cur = cur.next
        return dumphead.next
