"""
    Question:
    - https://leetcode.com/discuss/interview-question/372434

    Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. 
    Return the number of pairs.

    Example 1:

    Input: nums = [1, 1, 2, 45, 46, 46], target = 47
    Output: 2
    Explanation:
    1 + 46 = 47
    2 + 45 = 47
    Example 2:

    Input: nums = [1, 1], target = 2
    Output: 1
    Explanation:
    1 + 1 = 2
    Example 3:

    Input: nums = [1, 5, 1, 5], target = 6
    Output: 1
    Explanation:
    [1, 5] and [5, 1] are considered the same.
"""


def uniquePairs(nums, target):
    res = 0
    nums.sort()
    seen = set()
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            if (nums[i], nums[j]) not in seen:
                res += 1
                seen.add((nums[i], nums[j]))
            i += 1
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return res


# 2
a = [1, 1, 2, 45, 46, 46]
b = 47
print(uniquePairs(a, b))

# 1
a = [1, 1]
b = 2
print(uniquePairs(a, b))

# 1
a = [1, 5, 1, 5]
b = 6
print(uniquePairs(a, b))

# 1
a = [1, 2, 44, 46, 46, 46]
b = 47
print(uniquePairs(a, b))

# 3
a = [0, 1, 2, 45, 46, 47]
b = 47
print(uniquePairs(a, b))
