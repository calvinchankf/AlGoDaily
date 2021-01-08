"""
    2nd: linked list traversal
    - remember the prev node
    - go forward while cur.next.val == cur.val, assign prev.next = cur.next to skip the duplicate nodes

    Time    O(N)
    Space   O(1)
    44ms beats 41.95%
"""


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        dumphead = ListNode(2**32)
        dumphead.next = head
        prev = dumphead
        cur = head
        while cur != None:
            if cur.next != None and cur.next.val == cur.val:
                while cur.next != None and cur.next.val == cur.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dumphead.next
