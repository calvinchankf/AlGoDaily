"""
    1st: array

    Time    O(N)
    Space   O(1)
    32 ms, faster than 100.00%
"""


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        first = [0, 0]
        second = [-1, -1]
        for i in range(1, n):
            if nums[i] >= nums[i-1]:
                if second[0] == -1:
                    first[1] = i
                else:
                    second[1] = i
            elif second[0] == -1:
                second = [i, i]
            else:
                return False
        if first[0] == 0 and first[1] == n-1:
            return True
        if second[1] != n-1:
            return False
        return nums[n-1] <= nums[0]
