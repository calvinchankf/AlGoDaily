import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    2nd approach: reuse the sorted 2 lists

    Time    O(NK)
    Space   O(NK)
	5344 ms, faster than 7.60%
"""


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dump = ListNode(0)
        for x in lists:
            temp = self.merge2Lists(dump.next, x)
            dump.next = temp
        return dump.next

    def merge2Lists(self, l1, l2):
        cur1 = l1
        cur2 = l2
        dump = ListNode(0)
        curDump = dump
        while cur1 != None and cur2 != None:
            if cur1.val < cur2.val:
                curDump.next = cur1
                cur1 = cur1.next
            else:
                curDump.next = cur2
                cur2 = cur2.next
            curDump = curDump.next
        if cur1 != None:
            curDump.next = cur1
        if cur2 != None:
            curDump.next = cur2
        return dump.next


"""
    3rd approach: heap
	- iterate the list and put all the values into an array
	- sort the array
	- make that array into a linked list
    
	Time	O(NlogK)
	Space	O(K)
	100 ms, faster than 72.27%
"""


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        for head in lists:
            if head != None:
                heapq.heappush(pq, (head.val, head))
        
        dumphead = ListNode()
        cur = dumphead
        while len(pq) > 0:
            val, node = heapq.heappop(pq)
            cur.next = ListNode(val)
            cur = cur.next
            if node.next != None:
                nextNode = node.next
                heapq.heappush(pq, (nextNode.val, nextNode))
        return dumphead.next

"""
    Variation: merge k sort arrays iterator

    see /glassdoor/facebook/merge-sorted-lists-iterator
"""