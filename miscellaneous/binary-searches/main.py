def bsearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    # to find number that <= target
    # return right

    # to find number that >= target
    # return left

    return -1


print("--bsearch--")
print(bsearch([1, 3, 5, 7, 9], 4))   # -1
print(bsearch([1, 3, 5, 7, 9], 5))   # 2


def recursiveBsearch(nums, target):
    def f(nums, target, left, right):
        if left > right:
            return -1
        mid = (left+right)//2
        if target < nums[mid]:
            return f(nums, left, mid-1, target)
        elif target > nums[mid]:
            return f(nums, mid+1, right, target)
        return mid
    return f(nums, target, 0, len(nums)-1)


print("--recursiveBsearch--")
print(recursiveBsearch([1, 3, 5, 7, 9], 4))   # -1
print(recursiveBsearch([1, 3, 5, 7, 9], 5))   # 2


def bSearchNearest(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    # bounds checking
    if right < 0:
        return 0
    if left > len(nums)-1:
        return len(nums)-1
    # compare
    if abs(target-nums[right]) < abs(target-nums[left]):
        return right
    return left


print("--bSearchNearest--")
print(bSearchNearest([1, 3, 7, 13, 20], 4))   # 1
print(bSearchNearest([1, 3, 7, 13, 20], 5))   # 2


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


print("--lowerBsearch--")
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 0))   # 0
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 1))   # 0
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 4))   # 2 <- 4(taerget) is just <= 5(idx=2)
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 5))   # 2
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 6))   # 5 <- 6(target) is just <= 7(idx=5)
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 10))   # 7
# consider [1, 10, 23]
#      0    |    1    |    2
# -inf -> 1 | 2 -> 10 | 11 -> 23
# Or how many numbers < k

def upperBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if target >= nums[mid]:
            left = mid + 1
        else:
            right = mid
    return right


print("--upperBsearch--")
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 0))   # 0
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 1))   # 1
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 4))   # 2 <-
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 5))   # 5 
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 6))   # 5 <-
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 10))   # 7
# consider [1, 10, 23]
#      0    |   1    |    2
# -inf -> 0 | 1 -> 9 | 10 -> 23
# Or how many numbers <= k

def descending_bsearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if target < nums[mid]:
            # right = mid - 1
            left = mid + 1
        elif target > nums[mid]:
            # left = mid + 1
            right = mid - 1
        else:
            return mid
    # to find number that <= target
    # return right

    # to find number that no >= target
    # return left

    return -1


print("--descending_bsearch--")
print(descending_bsearch([11, 9, 7, 5, 3, 1], 4))   # -1
print(descending_bsearch([11, 9, 7, 5, 3, 1], 5))   # 2
print(descending_bsearch([11, 9, 7, 5, 3, 1], 7))   # 1


def descending_upperBsearch(nums, target):
    """
    [9, 7, 5, 5, 5, 3, 1]
                 ^
            find this
    """
    left = -1
    right = len(nums)-1
    while left < right:
        mid = (left + right + 1)//2
        if target <= nums[mid]:
            left = mid
        else:
            right = mid - 1
    return left


print("--descending_lowerBsearch--")
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 0))   # 6
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 1))   # 6
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 4))   # 4 <-
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 5))   # 4 <-
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 10))   # -1
