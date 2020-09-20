# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        while cur != None and cur.next != None:
            temp = cur.next
            cur.next = cur.next.next
            temp.next = head
            head = temp
        return head


for i in range(10):
    print(i)
print(i)
