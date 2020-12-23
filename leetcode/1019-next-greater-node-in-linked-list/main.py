# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    1st approach: stack
    - similar to lc503

    Time    O(2n)
    Space   O(n)
    344 ms, faster than 94.64%
"""


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        nums = []
        cur = head
        while cur != None:
            nums.append(cur.val)
            cur = cur.next
        # declaration
        stack = []
        res = len(nums) * [0]
        for i in range(len(nums)):
            num = nums[i]
            while len(stack) > 0 and num > stack[-1][0]:
                pop, idx = stack.pop()
                res[idx] = num
            stack.append((num, i))
        return res
