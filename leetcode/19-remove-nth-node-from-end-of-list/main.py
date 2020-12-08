
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    1st approach: 2 pointers + dump
    - the gap is the n such that when fast reaches to the end, slow.next is the target

    e.g. 
    
    list = 1 -> 2 -> 3 -> 4 -> 5, target = 4
    
    1 -> 2 -> 3 -> 4 -> 5
              ^         ^
            slow        fast

    Time		O(n+target)
    Space       O(1)
    24 ms, faster than 72.46%
"""


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n <= 0:
            return head
        dumphead = ListNode(0)
        dumphead.next = head
        slow = dumphead
        fast = dumphead
        for _ in range(n):
            fast = fast.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dumphead.next
