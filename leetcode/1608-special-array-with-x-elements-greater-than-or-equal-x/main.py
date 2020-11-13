"""
    1st: sort + binary search
    - for every number x from 0 to n, count the number of items that >= x

    Time    O(NlogN)
    Space   O(N)
    40 ms, faster than 50.00%
"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        counts = (n + 1) * [0]
        for i in range(n + 1):
            j = self.bsearch(nums, i)
            counts[i] = n - j
        for i in range(n+1):
            if counts[i] == i:
                return i
        return -1
    
    def bsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left