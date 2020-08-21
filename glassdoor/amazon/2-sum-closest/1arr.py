"""
    version1:
    Given an array of n integers, return a pair that closest, <=, to the target
    e.g. [2, 4, 10, 11, 6, 5, 9], 20
    return [9, 10]
"""


def optimalUtilization(nums, target):
    """
        classic approach: 2pointers
        - for each forward route, binary search through the return routes
        Time    O(2n)
        Space   O(n)
    """
    if target <= 0 or len(nums) == 0:
        return []
    nums = sorted(nums)
    # 2 poiters, binary search
    left = 0
    right = len(nums) - 1
    res = []
    best = 0
    while left < right:
        cur = nums[left] + nums[right]
        # result
        if cur > best and cur <= target:
            best = cur
            res = [nums[left], nums[right]]
        # binary search
        if cur > target:
            right -= 1
        else:
            left += 1
    return res


# [2, 4, 5, 6, 9, 10, 11]
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 20))
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 22))
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 12))
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 2))
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 1))
print("-----")
"""
    version2:
    Given an array of n integers, return ALL pairs that closest, <=, to the target
    e.g. [2, 4, 10, 11, 6, 5, 9], 11
    return [[2,9],[5,6]]
"""


def optimalUtilization(nums, target):
    """
        classic approach: 2pointers
        - for each forward route, binary search through the return routes
        Time    O(2n)
        Space   O(n)
    """
    if target <= 0 or len(nums) == 0:
        return []
    nums = sorted(nums)
    # 2 poiters, binary search
    left = 0
    right = len(nums) - 1
    res = []
    best = 0
    while left < right:
        cur = nums[left] + nums[right]
        # result
        if len(res) == 0:
            if cur <= target:
                best = cur
                res = [[nums[left], nums[right]]]
        elif cur <= target:
            if cur > best:
                best = cur
                res = [[nums[left], nums[right]]]
            elif cur == best:
                res.append([nums[left], nums[right]])
        # binary search
        if target < cur:
            right -= 1
        else:
            left += 1
    return res


# [2, 4, 5, 6, 9, 10, 11]
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 11))
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 20))
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 22))
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 12))
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 2))
print(optimalUtilization([2, 4, 10, 11, 6, 5, 9], 1))
