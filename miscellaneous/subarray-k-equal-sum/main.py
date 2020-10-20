"""
    Check if it possible to partition in k subarrays with equal sum

    e.g. nums = [1, 4, 2, 3, 5], K = 3
    return true

    because [1,4], [2,3], [5] <- sum of all non-empty subarrays equal to 5
"""


def kSubArrayEqualSum(nums, K):
    total = sum(nums)
    if total % K != 0:
        return False
    target = total//K

    cur = 0
    for i in range(len(nums)):
        cur += nums[i]
        if cur == target:
            cur = 0
            K -= 1
        elif cur > target:
            return False
    return K == 0


a = [1, 4, 2, 3, 5]
b = 3
print(kSubArrayEqualSum(a, b))

a = [1, 4, 2, 3, 6]
b = 3
print(kSubArrayEqualSum(a, b))

a = [1, 4, 2, 3, 6]
b = 3
print(kSubArrayEqualSum(a, b))

a = [1, 4, 2, 3, 6]
b = 2
print(kSubArrayEqualSum(a, b))

print("-----")
