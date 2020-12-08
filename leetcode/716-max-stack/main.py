"""
    1st approach: doubly linked list + binary search

    Time of
    - push()      O(logN + K)
    - pop()       O(logN + K)
    - top()       O(1)
    - peekMax()   O(1)
    - popMax()    O(logN + K)
    256 ms, faster than 17.40%
"""


class DLLNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.head = DLLNode(0)
        self.tail = DLLNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        last = self.tail.prev
        node = DLLNode(x)
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

        idx = self.upper_bsearch(self.nums, x)
        self.nums.insert(idx, (x, node))

    def pop(self):
        """
        :rtype: int
        """
        last = self.tail.prev
        last.prev.next = last.next
        last.next.prev = last.prev

        idx = self.upper_bsearch(self.nums, last.val)
        self.nums.pop(idx-1)
        return last.val

    def top(self):
        """
        :rtype: int
        """
        return self.tail.prev.val

    def peekMax(self):
        """
        :rtype: int
        """
        return self.nums[-1][0]

    def popMax(self):
        """
        :rtype: int
        """
        maxVal, maxNode = self.nums[-1]
        maxNode.prev.next = maxNode.next
        maxNode.next.prev = maxNode.prev

        idx = self.upper_bsearch(self.nums, maxVal)
        self.nums.pop(idx-1)
        return maxVal

    def upper_bsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target >= nums[mid][0]:
                left = mid + 1
            else:
                right = mid
        return left


"""
    Easier approach: sorted list + stack

    Time of
    - push()      O(logN + K)
    - pop()       O(logN + K)
    - top()       O(1)
    - peekMax()   O(1)
    - popMax()    O(K)
    148 ms, faster than 80.07%
"""


class MaxStack:

    def __init__(self):
        self.sortedNums = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        i = self._upperBsearch(self.sortedNums, x)
        self.sortedNums.insert(i, x)

    def pop(self) -> int:
        res = self.stack.pop()
        i = self._upperBsearch(self.sortedNums, res)
        self.sortedNums.pop(i-1)
        return res

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.sortedNums[-1]

    def popMax(self) -> int:
        res = self.sortedNums.pop()
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] == res:
                self.stack.pop(i)
                break
        return res

    def _upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right
