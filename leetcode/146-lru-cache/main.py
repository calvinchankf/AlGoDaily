from collections import *
"""
  Doubly Linked List + Hashtable
  - similar to lc379, lc1429

  Time  put:O(1), get: O(1)
  124ms beats 96.42%
"""


class ListNode(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.listCount = 0
        self.map = {}
        self.listHead = ListNode(-1, -1)
        self.listTail = ListNode(-1, -1)
        self.listHead.next = self.listTail
        self.listTail.prev = self.listHead

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            self._moveToTail(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._moveToTail(node)
            self.map[key] = node
        else:
            node = ListNode(key, value)
            self._addToTail(node)
            self.listCount += 1
            self.map[key] = node

        if self.listCount > self.capacity:
            firstKey = self._removeHead()
            del self.map[firstKey]
            self.listCount -= 1

    def _addToTail(self, node):
        last = self.listTail.prev
        last.next = node
        node.prev = last
        node.next = self.listTail
        self.listTail.prev = node

    def _moveToTail(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._addToTail(node)

    def _removeHead(self):
        # since we will check if self.listCount > self.capacity, we dont need to check if first would be listTail
        first = self.listHead.next
        self.listHead.next = first.next
        first.next.prev = self.listHead
        return first.key


c = LRUCache(2)
c.put("c", 123)
c.put("a", 456)
c.put("b", 789)
print(c.map)
c.put("a", 123)
print(c.listHead)
c.get("b")
c.get("b")
c.get("b")
print(c.listHead)

"""
    2nd approach: use orderdict

    Time of put():    O(1)
    Time of get():    O(1)
    940 ms, faster than 6.85%
"""


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.od = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.od:
            v = self.od[key]
            del self.od[key]
            self.od[key] = v
            return v
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
                firstKey = None
                for key in self.od:
                    firstKey = key
                    break
                del self.od[firstKey]


c = LRUCache(2)
c.put("c", 123)
c.put("a", 456)
c.put("b", 789)
print(c.od)
c.put("a", 123)
print(c.od)
c.get("b")
c.get("b")
c.get("b")
print(c.od)
