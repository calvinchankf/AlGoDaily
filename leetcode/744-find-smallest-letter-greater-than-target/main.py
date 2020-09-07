"""
    1st:uppper bound binary search

    Time    O(logN)
    Space   O(1)
    164 ms, faster than 27.15%
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = self.upperBsearch(letters, target)
        idx %= len(letters)
        return letters[idx]

    def upperBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return right
