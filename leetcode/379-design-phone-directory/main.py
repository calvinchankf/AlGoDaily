class DLLNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


"""
    1st approach: linked list + hashtable
    - similar to lc146, lc1429
    
    Time of init()      O(n)
    Time of others      O(1)
    Space               O(n)
    92 ms, faster than 56.15% 
"""


class PhoneDirectory(object):

    def __init__(self, n):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.cap = n
        self.count = 0
        self.head = DLLNode(-1)
        self.tail = DLLNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = set()
        for i in range(n):
            self._addToTail(i)

    def _addToTail(self, val):
        last = self.tail.prev
        node = DLLNode(val)
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
        self.m.add(val)
        self.count += 1

    def _removeHead(self):
        if self.count == 0:
            return -1
        first = self.head.next
        self.head.next = self.head.next.next
        first.next.prev = self.head
        self.count -= 1
        self.m.remove(first.val)
        return first.val

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        return self._removeHead()

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.m

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        if number < 0 or number+1 > self.cap or number in self.m:
            return
        self._addToTail(number)


"""
["PhoneDirectory", "check", "get", "check","get", "release", "check", "get", "get"]
[[1], [0], [], [0], [], [0], [0], [], []]

True
0
False
-1
None
True
0
-1
"""

# Your PhoneDirectory object will be instantiated and called as such:
obj = PhoneDirectory(1)
print(obj.check(0))
print(obj.get())
print(obj.check(0))
print(obj.get())
print(obj.release(0))
print(obj.check(0))
print(obj.get())
print(obj.get())

print("-----")

"""
["PhoneDirectory","get","get","check","get","check","release","check"]
[[3],[],[],[2],[],[2],[2],[2]]

0
1
True
2
False
None
True
"""
obj = PhoneDirectory(3)
print(obj.get())
print(obj.get())
print(obj.check(2))
print(obj.get())
print(obj.check(2))
print(obj.release(2))
print(obj.check(2))

"""
    2nd approach: just hashtable
    - takeaway: Set has a method, pop(), which release an arbitrary item from itself

    Time of init()      O(n)
    Time of others      O(1)
    Space               O(n)
    80 ms, faster than 94.63%
"""


class PhoneDirectory(object):
    def __init__(self, maxNumbers):
        self.cap = maxNumbers
        self.availables = set(range(maxNumbers))

    def get(self):
        if len(self.availables) > 0:
            return self.availables.pop()
        return -1

    def check(self, number):
        return number in self.availables

    def release(self, number):
        if number < 0 or number+1 > self.cap:
            return
        self.availables.add(number)
