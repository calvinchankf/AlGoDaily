"""
    1st: hashtable + linked list
    - similar to LRU

    Time of _evict()        O(N)
    Time of other func      O(1)
    Space                   O(N)
    140 ms, faster than 100.00%
"""


class ListNode(object):

    def __init__(self, key, time):
        self.key = key
        self.time = time
        self.prev = None
        self.next = None


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.length = 0
        self.map = {}
        self.head = ListNode('', -1)
        self.tail = ListNode('', -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _addToTail(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def _moveToTail(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._addToTail(node)

    def _evict(self, currentTime):
        while self.head.next.time <= currentTime - self.ttl and self.head.next != self.tail:
            first = self.head.next
            self.head.next = first.next
            first.next.prev = self.head
            self.length -= 1
            del self.map[first.key]

    def generate(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
        if tokenId in self.map:
            self.renew(tokenId, currentTime)
        else:
            newNode = ListNode(tokenId, currentTime)
            self._addToTail(newNode)
            self.map[tokenId] = newNode
            self.length += 1

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
        if tokenId not in self.map:
            return
        node = self.map[tokenId]
        node.time = currentTime
        self._moveToTail(node)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._evict(currentTime)
        return self.length
