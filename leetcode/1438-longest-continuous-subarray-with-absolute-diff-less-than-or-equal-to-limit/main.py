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
