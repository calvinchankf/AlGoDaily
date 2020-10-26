"""
    2nd: recursion

    Time    O(N)
    Space   O(N)
    32 ms, faster than 63.51%
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.swap(head)

    def swap(self, node):
        if node == None or node.next == None:
            return node
        dumphead = ListNode()
        a = node
        b = node.next
        c = None
        if node.next:
            c = node.next.next

        dumphead.next = b
        dumphead.next.next = a

        if c:
            dumphead.next.next.next = self.swap(c)
        else:
            dumphead.next.next.next = None

        return dumphead.next
