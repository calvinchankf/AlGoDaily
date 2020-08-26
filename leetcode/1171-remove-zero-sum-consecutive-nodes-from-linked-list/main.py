# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    1st: zero-sum subarray

    https://www.youtube.com/watch?v=hLcYp67wCcM

    generic approach
    - this question is fucking similar to leetcode 325, 523, 525, 560, 930, 1124
    - find loops <==============================================================
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: number of occurence of a previous sum
        - if currentSum - target in the hastable, the result+1

    Time	O(5n)
    Space   O(n)
    40 ms, faster than 52.22% 
"""


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        nums = []
        cur = head
        while cur != None:
            nums.append(cur.val)
            cur = cur.next

        ht = {}
        pfs = 0
        intvs = []
        for i in range(len(nums)):
            pfs += nums[i]
            if pfs == 0:
                intvs.append([0, i])
            if pfs in ht:
                intvs.append([ht[pfs]+1, i])
            ht[pfs] = i

        if len(intvs) == 0:
            return head

        intvs = sorted(intvs, key=lambda x: x[0])
        merged = [intvs[0]]
        for itv in intvs:
            if itv[0] <= merged[-1][1]:
                continue
            else:
                merged.append(itv)

        cands = len(nums)*[True]
        for intv in merged:
            start, end = intv[0], intv[1]
            for i in range(start, end+1):
                cands[i] = False

        newHead = ListNode(0)
        cur = newHead
        for i in range(len(cands)):
            if cands[i] == True:
                cur.next = ListNode(nums[i])
                cur = cur.next
        return newHead.next
