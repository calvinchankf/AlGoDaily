import sys
import heapq

"""
    1st: heap

    Time of init()          O(NlogK) N: all items, K: number of lists
    Time of hasNext()       O(1)
    Time of returnNext()    O(logK)
    Space                   O(K)
"""
class MergeListsIterator(object):
    def __init__(self, lists):
        self.pq = []
        for nums in lists:
            if len(nums) > 0:
                head = nums.pop(0)
                heapq.heappush(self.pq, (head, nums))

    def hasNext(self):
        return len(self.pq) > 0

    def returnNext(self):
        if not self.hasNext():
            return None
        head, nums = heapq.heappop(self.pq)
        if len(nums) > 0:
            nextHead = nums.pop(0)
            heapq.heappush(self.pq, (nextHead, nums))
        return head

a = [
    [1, 3, 6, 8],
    [2, 3, 5],
    [0, 4, 7]
]
s = MergeListsIterator(a)
for i in range(10):
    print(s.hasNext(), s.returnNext())
print(s.hasNext())

print("-----")

"""
    2nd: k pointers

    Time of init()          O(K)
    Time of hasNext()       O(K)
    Time of returnNext()    O(K)
    Space                   O(kN)
"""
class MergeListsIterator(object):
    def __init__(self, lists):
        self.lists = lists
        self.k = len(lists)
        self.pointers = self.k * [0]

    def hasNext(self):
        for i in range(self.k):
            nums = self.lists[i]
            if self.pointers[i] < len(nums):
                return True
        return False

    def returnNext(self):
        minPointer = -1
        minNum = sys.maxsize
        for i in range(self.k):
            j = self.pointers[i]
            nums = self.lists[i]
            if j < len(nums) and nums[j] < minNum:
                minNum = nums[j]
                minPointer = i
        self.pointers[minPointer] += 1
        return minNum

a = [
    [1, 3, 6, 8],
    [2, 3, 5],
    [0, 4, 7]
]
s = MergeListsIterator(a)
for i in range(10):
    print(s.hasNext(), s.returnNext())
print(s.hasNext())