"""
    1st: iteration
    - find the first element whose value is more than the length of remaining array,
    so we return the remaining length as the answer.


    Time    O(N)
    Space   O(1)
    132 ms, faster than 47.02%
"""


class Solution(object):
    def hIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for idx, c in enumerate(nums):
            if c >= n - idx:
                return n - idx
        return 0


"""
    1st: upper bound binary search
    - find the first element whose value is more than the length of remaining array,
    so we return the remaining length as the answer.

    Time    O(logN)
    Space   O(1)
    128 ms, faster than 66.67%
"""


class Solution(object):
    def hIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2

            # the element is less than the length of the remaining array,
            # the range is on the right excluding this element
            isNotMatched = nums[mid] < len(nums) - mid

            if isNotMatched:
                left = mid + 1
            else:
                right = mid
        # The element which value is more than the length of remaining array,
        # so we return the remaining length which is the answer
        return len(nums) - left
