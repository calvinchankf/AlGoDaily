from collections import Counter

"""
    1st: linked list + hashtable
    - similar to lc146

    Time of init                O(N)
    Time of showFirstUnique()   O(1)
    Time of add()               O(1)
    Space                       O(N)
    1128 ms, faster than 16.67%
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


"""
    2nd: queue + hashtable
    - not a very optimal approach
    - counter the occurence of each number
    - when we do showFirstUnique(), pop the queue until we reach to a number which appears once only

    Time of init                O(N)
    Time of showFirstUnique()   O(N)
    Time of add()               O(1)
    Space                       O(N)
    1532 ms, faster than 16.67%
"""


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.ht = {}
        self.q = []
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.ht[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        return self.q[0]

    def add(self, value: int) -> None:
        if value in self.ht:
            self.ht[value] += 1
        else:
            self.ht[value] = 1
            self.q.append(value)
