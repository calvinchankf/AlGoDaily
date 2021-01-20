# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


"""
    1st approach:
    1. use a hashtable to map the address of each node and a new node
    2. iterate the linked list and construct a new linked list using the values in hashtable

    Time    O(N)
    Space   O(N)
    68ms beats 97.59%
"""


class Solution(object):
    def copyRandomList(self, head):
        # put the addresses into a hashtable
        ht = {}
        cur = head
        while cur != None:
            ht[cur] = RandomListNode(cur.label)
            cur = cur.next
        # iterate the list again and construct a new list
        newhead = RandomListNode(-1)
        cur = head
        cloneCur = newhead
        while cur != None:
            node = ht[cur]
            if cur.random in ht:
                node.random = ht[cur.random]
            cloneCur.next = node
            cur = cur.next
            cloneCur = cloneCur.next
        return newhead.next


def printList(head):
    cur = head
    while cur != None:
        if cur.random != None:
            print(cur.label, cur.random.label)
        else:
            print(cur.label, None)
        cur = cur.next


a = RandomListNode(1)
b = RandomListNode(2)
c = RandomListNode(3)
d = RandomListNode(4)
a.next = b
b.next = c
c.next = d

a.random = c
d.random = a

s = Solution().copyRandomList(a)
printList(s)

print("-----")

"""
    2nd: do 1st recursively

    Time    O(N)
    Space   O(N)
    44 ms, faster than 54.79%
"""


class Solution(object):

    def __init__(self):
        self.cache = {}

    def copyRandomList(self, head):
        if head == None:
            return None
        if head in self.cache:
            return self.cache[head]
        clone = Node(head.val)
        self.cache[head] = clone
        clone.next = self.copyRandomList(head.next)
        clone.random = self.copyRandomList(head.random)
        return clone
