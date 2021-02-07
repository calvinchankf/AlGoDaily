from heapq import *
from bisect import insort_right, bisect_left

"""
    1st: sliding window + binary search
    - maintain a sorted array
    - during each iteration, pop the leftmost iteam of the sliding window in the sorted array 
        until the diff between sorted_arr[-1] - sorted_arr[0] <= limit


    e.g. nums = [5,2,7,8,1,10,100,4,4,4,4], limit = 5

    The sorted_arr in iterations:
    [5]
    [2, 5]
    [2, 5, 7]
    [7, 8]
    [1]
    [10]
    [100]
    [4]
    [4, 4]
    [4, 4, 4]
    [4, 4, 4, 4]


    Time    O(N^2 logN -> N^3)
    Space   O(N)
    1636 ms, faster than 5.07%
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        sorted_arr = []
        for i in range(len(nums)):
            num = nums[i]
            insort_right(sorted_arr, num)
            while sorted_arr[-1] - sorted_arr[0] > limit:
                leftmost_idx = i - len(sorted_arr) + 1
                target_idx = bisect_left(sorted_arr, nums[leftmost_idx])
                sorted_arr.pop(target_idx)
            # print(sorted_arr)
            res = max(res, len(sorted_arr))
        return res


"""
    2nd: optimize the 1st approach
    - the sorted_arry might not necessarily maintain the limit between sorted_arr[0] and sorted_arr[-1]
    
    e.g. nums = [5,2,7,8,1,10,100,4,4,4,4], limit = 5

    The sorted_arr in iterations:
    [5]
    [2, 5]
    [2, 5, 7]
    [2, 7, 8]
    [1, 7, 8]
    [1, 8, 10]
    [1, 10, 100]
    [4, 10, 100]
    [4, 4, 100]
    [4, 4, 4]
    [4, 4, 4, 4]

    Time    O(N^2)
    Space   O(N)
    700 ms, faster than 32.05%
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        sorted_arr = []
        for i in range(len(nums)):
            num = nums[i]
            insort_right(sorted_arr, num)
            if sorted_arr[-1] - sorted_arr[0] > limit:
                leftmost_idx = i - len(sorted_arr) + 1
                target_idx = bisect_left(sorted_arr, nums[leftmost_idx])
                sorted_arr.pop(target_idx)
            # print(sorted_arr)
            res = max(res, len(sorted_arr))
        return res


"""
    3rd: 2 heaps
    - minheap for the left
    - maxheap for the right
    - when the max - min > limit
        - move forward the slow pointer
        - pop the minheap, maxheap while the their indices are < slow pointer

    Time    O(NlogN)
    Space   O(N)
    1552 ms, faster than 11.25%
"""


class Solution(object):
    def longestSubarray(self, nums, limit):
        minheap = []
        maxheap = []
        j = 0  # slow pointer
        res = 0
        for i in range(len(nums)):
            x = nums[i]
            heappush(minheap, (x, i))
            heappush(maxheap, (-x, i))
            while -maxheap[0][0] - minheap[0][0] > limit:
                j = min(minheap[0][1], maxheap[0][1]) + 1
                while minheap[0][1] < j:
                    heappop(minheap)
                while maxheap[0][1] < j:
                    heappop(maxheap)
            res = max(res, i - j + 1)
        return res
