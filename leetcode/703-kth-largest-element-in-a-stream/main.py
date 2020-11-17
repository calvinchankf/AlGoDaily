
import heapq

"""
    1st approach: binary search the upper bound

    Time    O(nlogn) __init__, O(logn) add
    Space   O(n)
    188 ms, faster than 26.90%
"""


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.nums = sorted(nums)
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        pos = upperBSearch(self.nums, val)
        self.nums.insert(pos, val)
        return self.nums[len(self.nums)-k]

    def upperBSearch(nums, target):
        left = 0
        right = len(self.nums)
        while left < right:
            mid = (left + right)/2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right


"""
    2nd approach: use a min heap with capacity
    - similar to lc215, 703

    let's say k = 4, start with [2,1,3,1]

    .add(5)     [2,1,3,1,5] -> [2,3,1,5]
    .add(7)     [1,2,3,5,7] -> [2,3,5,7]
    .add(2)     [2,3,5,7,2] -> [2,3,5,7]
    .add(6)     [2,3,5,7,6] -> [3,5,7,6]

    therefore, it means it always keep the K largest numbers in an unsorted order

    Time    O(n) __init__, O(logn) add
    Space   O(n)
    100 ms, faster than 61.58%
"""


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


"""
    followup1: kth smallest

    approach: max heap
"""
