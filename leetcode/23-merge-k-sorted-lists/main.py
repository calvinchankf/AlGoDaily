import heapq


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    2nd approach: reuse the sorted 2 lists

    Time    O(nk)
    Space   O(nk)
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
    3rd approach: heap (its actually=sort)
	- iterate the list and put all the values into an array
	- sort the array
	- make that array into a linked list
    
	Time	O(Nlogk)
	Space	O(N)
	124 ms, faster than 41.48% 
"""


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        for l in lists:
            cur = l
            while cur != None:
                heapq.heappush(pq, cur.val)
                cur = cur.next
        dump = ListNode(0)
        cur = dump
        while len(pq) > 0:
            pop = heapq.heappop(pq)
            node = ListNode(pop)
            cur.next = node
            cur = cur.next
        return dump.next
