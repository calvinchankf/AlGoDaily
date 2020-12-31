# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
    2nd approach: inplace replacement(learned from others)

    idea:
	1->2->3->4
    2->1->3->4
    3->2->1->4
    4->3->2->1

    ref:
    - https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1204/
    
	Time		O(n)
    Space 	    O(1) since in-place
    32 ms, faster than 88.70%
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newHead = head
        while head != None and head.next != None:
            temp = head.next
            head.next = head.next.next
            temp.next = newHead
            newHead = temp
        return newHead


for i in range(10):
    print(i)
print(i)
