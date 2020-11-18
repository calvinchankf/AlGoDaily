import heapq

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
    - similar to lc215, 703
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


"""
    3rd: quick select

    Time		O(N) -> O(N^2)
	Space		O(N)
	80 ms, faster than 48.50%
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
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
    followup1: kth smallest
    followup2: distinct
"""
