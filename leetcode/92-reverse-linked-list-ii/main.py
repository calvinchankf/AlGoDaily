# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode

        1st approach
        - similar to reverse linked list and reverse halh of a linked list
        - we need to find the parent of node[m] first, reverse the later list until the count < n(right)
        20ms beats 100%
        29jan2019
        """
        # find the parent of node[m]
        dumphead = ListNode(0)
        dumphead.next = head

        parent = dumphead
        cur = head
        count = 1
        while count < m and cur != None:
            parent = cur
            cur = cur.next
            count += 1
        # reverse the linked list until n
        newHead = cur
        while cur != None and cur.next != None and count < n:
            temp = cur.next
            cur.next = cur.next.next
            temp.next = newHead
            newHead = temp
            count += 1
        parent.next = newHead
        return dumphead.next


# helpers for test
def arr2list(arr):
    dump = ListNode(0)
    dumpCur = dump
    for i in range(len(arr)):
        dumpCur.next = ListNode(arr[i])
        dumpCur = dumpCur.next
    return dump.next


def printList(l):
    c = l
    acc = ""
    while c != None:
        acc += str(c.val)+','
        c = c.next
    print(acc)


a = arr2list([])
s = Solution().reverseBetween(a, 0, 0)
printList(s)

a = arr2list([1])
s = Solution().reverseBetween(a, 1, 1)
printList(s)

a = arr2list([1, 2, 3, 4, 5])
s = Solution().reverseBetween(a, 2, 4)
printList(s)

a = arr2list([1, 2, 3, 4, 5])
s = Solution().reverseBetween(a, 2, 5)
printList(s)

a = arr2list([1, 2, 3, 4, 5])
s = Solution().reverseBetween(a, 1, 4)
printList(s)

a = arr2list([1, 2, 3, 4, 5])
s = Solution().reverseBetween(a, 1, 5)
printList(s)
