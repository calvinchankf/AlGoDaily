# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
    1. reverse the 2nd half of the linked list
    2. compare

    Time    O(3N)
    Space   O(1)
"""


def linkedListPalindrome(head):
    if not head:
        return None
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    r = reverseLinkedList(mid)
    cur1 = head
    cur2 = r
    while cur1 != None and cur2 != None:
        if cur1.value != cur2.value:
            return False
        cur1 = cur1.next
        cur2 = cur2.next
    return True


def reverseLinkedList(head):
    nextHead = head
    while head != None and head.next != None:
        temp = head.next
        head.next = head.next.next
        temp.next = nextHead
        nextHead = temp
    return nextHead
