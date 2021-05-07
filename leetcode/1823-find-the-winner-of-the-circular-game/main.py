"""
    1st: linked list
    - I was asked the same question by Goldman Sachs, they called it "musical chairs"

    e.g.1
    
    N = 4, K = 2

    1 2 3 4
    * ^     start at 1, stop at 2, then we remove 2

    1 3 4
      * ^   start at 3, stop at 4, then we remove 4

    1 3
    * ^     start at 1, stop at 3, then we remove 3

    1       answer

    e.g.2
    N = 6, K = 4

    1 2 3 4 5 6
    *     ^     start at 1, stop at 4 , then we remove 4

    1 2 3 5 6
      ^   *     start at 5, stop at 2 , then we remove 2

    1 3 5 6
    ^ *         start at 3, stop at 1 , then we remove 1

    3 5 6
    *
    ^           start at 3, stop at 3 , then we remove 3

    5 6
    * ^         start at 5, stop at 6 , then we remove 6

    5           answer

    e.g.3
    N = 2, K = 2
    1 2
    * ^     start at 1, stop at 2, then we remove 2

    1           answer

    Time    O(N)
    Space   O(N) the linked list
    180 ms, faster than 33.51%
"""


class ListNode:
    def __init__(self, val=-1):
        self.val = val
        self.next = None


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k < 2:
            return n
        head = ListNode(1)
        cur = head
        for i in range(2, n+1):
            cur.next = ListNode(i)
            cur = cur.next
        cur.next = head

        cur = head
        while cur.next != cur:
            for i in range(k-2):
                cur = cur.next
            cur.next = cur.next.next
            cur = cur.next
        return cur.val
