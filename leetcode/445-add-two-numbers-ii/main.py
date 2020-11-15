# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    1st approach: 2 stacks
	1. put the values into its corresponding stack
	2. pop the stacks, and sum up the numbers with carry
	3. if there is a carry, add 1

	Time	O(2m+2n)
	Space	O(m+n)
	72 ms, faster than 27.17%
"""


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = self.getStack(l1)
        stack2 = self.getStack(l2)
        cur = None
        carry = 0
        while len(stack1) > 0 or len(stack2) > 0 or carry > 0:
            a = 0
            if len(stack1) > 0:
                a = stack1.pop()
            b = 0
            if len(stack2) > 0:
                b = stack2.pop()
            temp = a + b + carry
            d = temp % 10
            carry = temp//10
            newHead = ListNode(d)
            newHead.next = cur
            cur = newHead
        return cur

    def getStack(self, l):
        stack = []
        cur = l
        while cur != None:
            stack.append(cur.val)
            cur = cur.next
        return stack
