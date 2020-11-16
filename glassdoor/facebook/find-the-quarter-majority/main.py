"""
    https://leetcode.com/discuss/interview-question/627483/facebook-phone-find-the-quarter-majority

    Given a sorted array of size n, find the majority element. 
    The majority element is the element that appears more than n/4 times. 
    You may assume that the array is non-empty and the majority element always exist in the array.

    Example 1:
    Input: [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7]
    Output: 3

    Example 2:
    Input: [1, 1, 2, 2, 3, 3, 4, 5, 7, 7, 7]
    Output: 7

    Example 3:
    Input: [1, 1, 2, 3]
    Output: 1
"""


def findQuarterMajority(nums):
    n = len(nums)
    windowSize = n // 4
    for i in range(0, n, windowSize):
        left = lowerBsearch(nums, nums[i])
        right = left + windowSize
        if nums[left] == nums[right]:
            return nums[i]
    return None


def lowerBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left


a = [1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 7]
print(findQuarterMajority(a))

a = [1, 1, 2, 2, 3, 3, 4, 5, 7, 7, 7]
print(findQuarterMajority(a))

a = [1, 1, 2, 3]
print(findQuarterMajority(a))

a = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
print(findQuarterMajority(a))

a = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4]
print(findQuarterMajority(a))

a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]
print(findQuarterMajority(a))

a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(findQuarterMajority(a))
