from heapq import *

"""
    1st approach: upper bound binary search

    Time    O(n * (logk + k)) since insert takes O(k)
    Space   O(k)
    112 ms, faster than 33.23%
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 or k <= 0:
            return -1
        window = []
        for num in nums:
            idx = self.upperbsearch(window, num)
            window.insert(idx, num)
            if len(window) > k:
                window.pop(0)
        return window[0]

    def upperbsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


"""
    2nd approach: min heap
    - similar to lc215, 703, 973
    - maintain a min heap of size k, the top item in the minheap at the end is the kth largest item

	Time		O(NlogK)
	Space		O(n)
	72 ms, faster than 40.76%
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 or k <= 0:
            return -1
        minHeap = []
        for x in nums:
            heappush(minHeap, x)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]


s = Solution()

a = [3, 2, 1, 5, 6, 4]
b = 2
print(s.findKthLargest(a, b))

# [1, 2, 2, 3, 3, 4, 5, 5, 6]
#                 ^
a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
b = 4
print(s.findKthLargest(a, b))

print("-----")

"""
    3rd: quick select

    Time		O(N) -> O(N^2)
	Space		O(N)
	80 ms, faster than 48.50%
"""


class Solution:
    def findKthLargest(self, nums, k):
        return self.quickSelect(nums, 0, len(nums)-1, k)

    def quickSelect(self, nums, left, right, k):
        if k > 0 and k <= len(nums):
            pIdx = self.partition(nums, left, right)
            if pIdx+1 == k:
                return nums[pIdx]
            elif pIdx+1 < k:
                return self.quickSelect(nums, pIdx+1, right, k)
            else:
                return self.quickSelect(nums, left, pIdx-1, k)
        return -1

    def partition(self, nums, left, right):
        pivot = nums[right]
        pIdx = left
        for i in range(left, right):
            if nums[i] >= pivot:
                nums[i], nums[pIdx] = nums[pIdx], nums[i]
                pIdx += 1
        nums[pIdx], nums[right] = nums[right], nums[pIdx]
        return pIdx


"""
    followup1: distinct
    followup2: do we have to put all the items in to the heap?
    followup3: k = N - 100 if N = 10B
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        # followup1: distinct
        if len(nums) == 0 or k <= 0:
            return -1
        seen = set()
        minHeap = []
        for x in nums:
            if x in seen:
                continue
            seen.add(x)
            heappush(minHeap, x)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]


s = Solution()

a = [3, 2, 1, 5, 6, 4]
b = 2
print(s.findKthLargest(a, b))

# [1, 2, 3, 4, 5, 6]
#        ^
a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
b = 4
print(s.findKthLargest(a, b))

print("-----")


class Solution(object):
    def findKthLargest(self, nums, k):
        # followup2: do we have to put all the items in to the heap?
        minHeap = []
        for x in nums:
            if len(minHeap) == k and x < minHeap[0]:
                continue
            heappush(minHeap, x)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]


s = Solution()

a = [3, 2, 1, 5, 6, 4]
b = 2
print(s.findKthLargest(a, b))

# [1, 2, 3, 4, 5, 6]
#        ^
a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
b = 4
print(s.findKthLargest(a, b))

print("-----")


class Solution(object):
    def findKthLargest(self, nums, k):
        """
            followup3: k = N - 100 if N = 1000b

            Time    O(NlogK)
            Space   O(N/2)
            56 ms, faster than 55.93%
        """
        if k <= len(nums) - k + 1:
            minHeap = []
            for x in nums:
                if len(minHeap) == k and x < minHeap[0]:
                    continue
                heappush(minHeap, x)
                if len(minHeap) > k:
                    heappop(minHeap)
            return minHeap[0]
        # if K is large, then it is actually finding the N-K+1 smallest element, then we can use a maxHeap
        maxHeap = []
        for x in nums:
            if len(maxHeap) == len(nums) - k + 1 and x > -maxHeap[0]:
                continue
            heappush(maxHeap, -x)
            if len(maxHeap) > len(nums) - k + 1:
                heappop(maxHeap)
        return -maxHeap[0]


s = Solution()

# [1, 2, 3, 4, 5, 6]
#  ^
a = [3, 2, 1, 5, 6, 4]
b = 6
print(s.findKthLargest(a, b))

# [1, 2, 2, 3, 3, 4, 5, 5, 6]
#     ^
a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
b = 8
print(s.findKthLargest(a, b))

print("-----")
