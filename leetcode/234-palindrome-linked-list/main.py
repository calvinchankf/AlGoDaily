# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    2nd approach: 2 pointers
    - slow walks 1 step at a time, fast walks 2 steps at a time
    - slow stops at the node points to the 2nd half
    - reverse the 2nd half
    - traverse the 1st half and the 2nd half to see if the values equal

    Time    O(2n)
    Space   O(1)
    72 ms, faster than 93.58%
"""


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        # find the half
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # reverse the 2nd half
        head2 = self.reverse(slow)
        # check if 1st half == 2nd half
        cur1 = head
        cur2 = head2
        while cur1 != None and cur2 != None:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True
        
    def reverse(self, head):
        newHead = head
        while head.next != None:
            temp = head.next
            head.next = head.next.next
            temp.next = newHead
            newHead = temp
        return newHead