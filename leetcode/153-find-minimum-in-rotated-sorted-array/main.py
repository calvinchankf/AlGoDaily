"""
    easier to understand: always look for the pivot point
    1. if the left most number is less than the right most number, the left most is the result
    2. if not, look for the pivot point with binary search

    Time    O(logn)
    Space   O(1)
    12 ms, faster than 100.00%
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            # if no left most < right most, the minval is the left most number
            if nums[left] <= nums[right]:
                return nums[left]

            # binary search, always keep the mid
            # e.g.1
            # 4, 5, 1, 2, 3
            #       ^
            # 4, 5, 1     <- next iteration
            mid = (left + right)//2
            # both < and <= work fine because there are duplicate numbers
            if nums[mid] <= nums[right]:
                right = mid
            else:
                # e.g.1
                # 4, 5, 6, 7, 8, 1, 2
                #          ^
                #             8, 1, 2 <- next iteration
                # e.g.2
                # 4, 5, 6, 7, 1, 2
                #          ^
                #             1, 2 <- next iteration
                left = mid + 1


"""
    variation: find max

    Approach: same as above except return j-1
    Since maxNum is always on the left of the minNum, we just need to return the nums[(left - 1) % n]
"""


class Solution(object):
    def findMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            # if no left most < right most, the minval is the left most number
            if nums[left] <= nums[right]:
                return nums[(left - 1) % n]
            # binary search, always keep the mid
            mid = (left + right)//2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1


a = [3, 4, 5, 1, 2]
print(Solution().findMax(a))

a = [5, 6, 0, 1, 2, 3, 4]
print(Solution().findMax(a))

a = [6, 0, 1, 2, 3, 4, 5]
print(Solution().findMax(a))

a = [2, 1]
print(Solution().findMax(a))

a = [1, 2]
print(Solution().findMax(a))

a = [1, 2, 3, 4, 5, 6]
print(Solution().findMax(a))
