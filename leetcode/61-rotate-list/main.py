# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    1st: linked list traversal
    1. find the length
    2. find the node link to cut
    3. put the 2nd half to the front of the linked list

    Time    O(N)
    Space   O(1)
    32 ms, faster than 94.23%
"""


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        elif head.next == None:
            return head
        elif k == 0:
            return head
        # find the length
        # find the last node
        n = 0
        last = None
        cur = head
        i = 0
        while cur != None:
            n += 1
            last = cur
            cur = cur.next
        # find the node link to cut
        # and put the 2nd half to the front of the linked list
        k %= n
        if k == 0:
            return head
        target = n - k
        cur = head
        i = 0
        secondHalf = None
        while cur != None:
            i += 1
            if i == target:
                secondHalf = cur.next
                cur.next = None
                break
            cur = cur.next

        dumpHead = ListNode(0)
        dumpHead.next = secondHalf
        last.next = head
        return dumpHead.next
