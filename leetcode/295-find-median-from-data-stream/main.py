import heapq

"""
    1st approach: heap
    - LTE

    2nd approach: BST
    - LTE
"""

"""
    3rd approach: 2 heaps
    - maxheap for left half
    - minheap for right half
    - therefore the mean will always be the max of maxheap and the min of minheap
    - https://leetcode.com/articles/find-median-from-data-stream/

    always maintain the maxheap <= minheap in size

    308 ms, faster than 55.77%
"""


class MedianFinder(object):

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num):
        if len(self.maxheap) == len(self.minheap):
            heappush(self.maxheap, -num)
            x = -heappop(self.maxheap)
            heappush(self.minheap, x)
        else:
            heappush(self.minheap, num)
            x = heappop(self.minheap)
            heappush(self.maxheap, -x)

    def findMedian(self):
        if len(self.maxheap) == len(self.minheap):
            left = -self.maxheap[0]
            right = self.minheap[0]
            return (left + right) / 2.0
        else:
            return self.minheap[0]


obj = MedianFinder()
obj.addNum(1)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(1)
obj.addNum(3)
obj.addNum(2)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(5)
obj.addNum(3)
obj.addNum(4)
obj.addNum(3)
obj.addNum(1)
obj.addNum(2)
obj.addNum(6)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("========================================")

"""
    3rd approach2: 2 heaps
    - maxheap for left half
    - minheap for right half
    - therefore the mean will always be the max of maxheap and the min of minheap
    - https://leetcode.com/articles/find-median-from-data-stream/

    always maintain the maxheap >= minheap in size

    308 ms, faster than 55.77%
"""


class MedianFinder(object):

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num):
        """
        O(logn)
        """
        if len(self.maxheap) == len(self.minheap):
            # push to right, pop right, push to left such that left will be larger
            heapq.heappush(self.minheap, num)
            leastOnRight = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -leastOnRight)
        else:
            # push to left, pop left, push to right such that left len == right len
            heapq.heappush(self.maxheap, -num)
            largestOnLeft = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -largestOnLeft)

    def findMedian(self):
        """
        O(1)
        """
        if len(self.maxheap) != len(self.minheap):
            return -self.maxheap[0]
        return (-self.maxheap[0] + self.minheap[0])/2.0


obj = MedianFinder()
obj.addNum(1)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(1)
obj.addNum(3)
obj.addNum(2)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("---")

obj = MedianFinder()
obj.addNum(5)
obj.addNum(3)
obj.addNum(4)
obj.addNum(3)
obj.addNum(1)
obj.addNum(2)
obj.addNum(6)
print(obj.maxheap)
print(obj.minheap)
print(obj.findMedian())

print("========================================")

"""
    4th approach: upper bound binary search
    - add the number in correct position
    - find median from the half of the array

    Time    O(n) because list.insert() takes O(n)
    Space   O(n)
    336 ms, faster than 45.33%
"""


class MedianFinder(object):

    def __init__(self):
        self.sorted = []

    def addNum(self, num):
        """
        O(logn)
        """
        i = self._upperBSearch(num)
        self.sorted.insert(i, num)

    def _upperBSearch(self, target):
        left = 0
        right = len(self.sorted)
        while left < right:
            mid = (left + right)//2
            if target >= self.sorted[mid]:
                left = mid + 1
            else:
                right = mid
        return left

    def findMedian(self):
        """
        O(1)
        """
        if len(self.sorted) % 2 == 0:
            mid = (len(self.sorted)-1)/2
            left = self.sorted[mid]
            right = self.sorted[mid+1]
            return (left + right)/2.0
        mid = (len(self.sorted)-1)/2
        return self.sorted[mid]*1.0
