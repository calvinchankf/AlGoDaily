# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    2nd approach: same idea as 1st approach but shorter

	Time	O(l+r)
	Space	O(l+r) the result
	12ms beats 100%
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dumphead = ListNode()
        cur = dumphead
        cur1 = l1
        cur2 = l2
        while cur1 != None or cur2 != None:
            a = 0
            if cur1 != None:
                a = cur1.val
                cur1 = cur1.next
            b = 0
            if cur2 != None:
                b = cur2.val
                cur2 = cur2.next
            d = (a + b + carry)%10
            carry = (a + b + carry)//10
            cur.next = ListNode(d)
            cur = cur.next
        if carry > 0:
            cur.next = ListNode(carry)
        
        return dumphead.next
