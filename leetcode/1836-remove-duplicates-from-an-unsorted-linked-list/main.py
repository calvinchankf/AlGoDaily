
from collections import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    1st: hashtable
    - just count of frequency of every node.val
    - build the result linkedlist with nodes who appear once

    Time    O(N)
    Space   O(N)
    1464 ms, faster than 100.00%
"""


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counter = Counter()
        cur = head
        while cur != None:
            counter[cur.val] += 1
            cur = cur.next
        dumphead = ListNode()
        dumpCur = dumphead
        cur = head
        while cur != None:
            if counter[cur.val] == 1:
                dumpCur.next = ListNode(cur.val)
                dumpCur = dumpCur.next
            cur = cur.next
        return dumphead.next
