from collections import Counter

"""
    1st: linked list + hashtable
    - similar to lc146

    Time of init                O(N)
    Time of showFirstUnique()   O(N)
    Time of add()               O(N)
    Space                       O(N)
    1088 ms
"""


class ListNode(object):

    def __init__(self, key: int):
        self.key = key
        self.prev = None
        self.next = None


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.map = {}
        self.listHead = ListNode(-1)
        self.listTail = ListNode(-1)
        self.listHead.next = self.listTail
        self.listTail.prev = self.listHead

        counter = Counter(nums)
        for x in nums:
            if counter[x] == 1:
                node = ListNode(x)
                self.map[x] = node
                self._addToTail(node)
            else:
                self.map[x] = -1

    def _addToTail(self, node):
        last = self.listTail.prev
        last.next = node
        node.prev = last
        node.next = self.listTail
        self.listTail.prev = node

    def _removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def showFirstUnique(self) -> int:
        if self.listHead.next == self.listTail:
            return -1
        return self.listHead.next.key

    def add(self, value: int) -> None:
        if value in self.map:
            node = self.map[value]
            if node != -1:
                self._removeFromList(node)
        else:
            node = ListNode(value)
            self.map[value] = node
            self._addToTail(node)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
