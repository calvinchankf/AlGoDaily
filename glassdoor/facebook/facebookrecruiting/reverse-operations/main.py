class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# logic here


def reverse(head):
    dumphead = Node(0)
    dumphead.next = head
    cur = dumphead
    while cur != None:
        if cur.next != None and cur.next.data % 2 == 0:
            _head, _tail = reverseLinkedList(cur.next)
            cur.next = _head
            cur = _tail
        cur = cur.next
    return dumphead.next


def reverseLinkedList(head):
    newHead = head
    while head.next != None and head.next.data % 2 == 0:
        temp = head.next
        head.next = head.next.next
        temp.next = newHead
        newHead = temp
    return newHead, head


# helpers
def _createLinkedList(arr):
    head = None
    tempHead = head
    for v in arr:
        if head == None:
            head = Node(v)
            tempHead = head
        else:
            head.next = Node(v)
            head = head.next
    return tempHead


def _printLinkedList(head):
    res = []
    cur = head
    while cur != None:
        res.append(cur.data)
        cur = cur.next
    print(res)
# a = _createLinkedList([2, 4, 6, 8, 1])
# b, c = reverseLinkedList(a)
# _printLinkedList(b)
# print(c.data)


a = [1, 2, 8, 9, 12, 16]
b = _createLinkedList(a)
_printLinkedList(reverse(b))

a = [2, 18, 24, 3, 5, 7, 9, 6, 12]
b = _createLinkedList(a)
_printLinkedList(reverse(b))

a = [1, 3, 2, 4, 6, 7, 9]
b = _createLinkedList(a)
_printLinkedList(reverse(b))
