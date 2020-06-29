# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
    1st: linked list traversal

    Time    O(N)
    Space   O(N)
    64 ms, faster than 100.00%
"""


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dumpHead = ListNode()
        dumpHead.next = head
        cur = dumpHead
        i = 0
        while cur.next != None:
            cur = cur.next
            i += 1
            if i == m:
                j = 0
                temp = cur
                while j < n and temp != None:
                    temp = temp.next
                    j += 1
                if temp != None:
                    cur.next = temp.next
                else:
                    cur.next = None
                i = 0
        return dumpHead.next
