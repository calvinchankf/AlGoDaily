# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
    2nd approach: dont count the linked list in constructor, do it in getRandom()

    Time  O(1) constructor(), O(2n) getRandom(): traverse + random
    Space O(n)
    92 ms, faster than 67.61%
"""


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cnt = 0
        cur = self.head
        while cur != None:
            cnt += 1
            cur = cur.next
        node = self.head
        r = random.randrange(cnt)
        for _ in range(r):
            node = node.next
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

"""
    3rd approach: Reservoir Sampling
    - for an unknown size array or data stream, we can do Reservoir Sampling such that we dont need to store the size of the array initially
    e.g. [x1,x2,x3,x4,x5,.......]

    the calculation of probability: selected * notselected * notselected * notselected..... * notselected

    Therefore...
    the prob of x1 = 1/1 * 1/2 * 2/3 * 3/4 * ..... * (n-1)/n = 1/n
    the prob of x2 = 1/2 * 2/3 * 3/4 * ..... * (n-1)/n = 1/n
    the prob of x3 = 1/3 * 3/4 * ..... * (n-1)/n = 1/n
    ...
    the prob of x(n-1) = 1/(n-1) * (n-1)/n = 1/n
    the prob of xn = 1/n = 1/n

    ref:
    - https://www.jianshu.com/p/63f6cf19923d

    Time    O(1) constructor, O(n) pick
    Space   O(n) input linked list
    180 ms, faster than 54.55%
"""


class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        cnt = 1
        cur = self.head
        res = self.head
        while cur != None:
            # for any number i,
            # the prob = selected * notselected * notselected * notselected..... * notselected
            # the prob of xi = 1/i * (i+1)/(i+2) * ..... * (n-1)/n = 1/n
            if random.randrange(cnt) == 0:
                res = cur
            cnt += 1
            cur = cur.next
        return res.val
