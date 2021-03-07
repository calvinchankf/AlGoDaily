# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    1st: brute force

    Time    O(2N)
    Space   O(N)
    1836 ms, faster than 15.49%
"""


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        nums = []
        cur = head
        while cur != None:
            nums.append(cur.val)
            cur = cur.next
        n = len(nums)
        nums[k-1], nums[n-k] = nums[n-k], nums[k-1]
        dumphead = ListNode(-1)
        cur = dumphead
        for x in nums:
            cur.next = ListNode(x)
            cur = cur.next
        return dumphead.next
