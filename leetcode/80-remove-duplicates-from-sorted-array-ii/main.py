"""
    2nd approach: 2 pointers
    - similar to lc26, 75, 283
    - slow pointer points to the right most distinct number
    - fast pointer is for iteration
    - if fast pointer meets a different value, slow pointer move forward and modify the numer as the fast pointer points to

    Time    O(n)
    Space   O(1)
    76 ms, faster than 32.29%
"""


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        j = 0
        curMax = -sys.maxsize
        curCount = 0
        for i in range(len(nums)):
            if nums[i] > curMax:
                curMax = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                curCount = 1
            elif nums[i] == curMax and curCount < 2:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                curCount += 1
        return j


a = [1, 1, 1, 2, 2, 3]
print(Solution().removeDuplicates(a))
print(a)

a = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(a))
print(a)
