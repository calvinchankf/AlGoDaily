# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    1st:
    - reverse the input linked list
    - do math to compute the result

    Time    O(2N)
    Space   O(1)
    20 ms, faster than 100.00%
"""


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = 0
        tempList = self.reverseList(head)
        res = 0
        i = 0
        while tempList != None:
            res += (2**i) * tempList.val
            tempList = tempList.next
            i += 1
        return res

    def reverseList(self, head):
        newHead = head
        while head != None and head.next != None:
            temp = head.next
            head.next = head.next.next
            temp.next = newHead
            newHead = temp
        return newHead


"""
    2nd:
    - do math directly to compute the result
    e.g. 1011
    2*0 + 1 = 1
    2*1 + 0 = 2
    2*2 + 1 = 5
    2*5 + 1 = 11

    Time    O(2N)
    Space   O(1)
    20 ms, faster than 100.00%
"""


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = 0
        while head:
            res = 2*res + head.val
            head = head.next
        return res
