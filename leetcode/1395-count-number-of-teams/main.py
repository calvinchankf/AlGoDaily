"""
    1st: array
    - for each number
        - count the number of items less then itself from the left
        - count the number of items bigger then itself from the right
    - same idea vice versa

    Time    O(n^2)
    Space   O(1)
    60 ms, faster than 97.67%
"""


class Solution:
    def numTeams(self, nums: List[int]) -> int:
        res = 0
        for j in range(1, len(nums)-1):
            left_smaller_count = 0
            left_bigger_count = 0
            for i in range(j):
                if nums[i] < nums[j]:
                    left_smaller_count += 1
                elif nums[i] > nums[j]:
                    left_bigger_count += 1
            right_smaller_count = 0
            right_bigger_count = 0
            for k in range(j+1, len(nums)):
                if nums[j] < nums[k]:
                    right_bigger_count += 1
                elif nums[j] > nums[k]:
                    right_smaller_count += 1
            res += left_smaller_count * right_bigger_count
            res += left_bigger_count * right_smaller_count
        return res
