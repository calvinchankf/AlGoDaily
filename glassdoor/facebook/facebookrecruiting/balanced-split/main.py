"""
    Given an array of integers (which may include repeated integers), 
    determine if there's a way to split the array into two subsequences A and B such that the sum of the integers in both arrays is the same, 
    and all of the integers in A are strictly smaller than all of the integers in B.
    
    Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.

    Example 1
    arr = [1, 5, 7, 1]
    output = true
    We can split the array into A = [1, 1, 5] and B = [7].
    
    Example 2
    arr = [12, 7, 6, 7, 6]
    output = false
    We can't split the array into A = [6, 6, 7] and B = [7, 12] since this doesn't satisfy the requirement that all integers in A are smaller than all integers in B.
"""


def balancedSplitExists(arr):
    arr.sort()
    total = sum(arr)
    pfs = 0
    for i in range(len(arr)-1):
        pfs += arr[i]
        total -= arr[i]
        if pfs == total and arr[i] != arr[i+1]:
            return True
    return False


# T
a = [2, 1, 2, 5]
print(balancedSplitExists(a))

# F
a = [12, 7, 6, 7, 6]
print(balancedSplitExists(a))

# T
a = [2, 1, 2, 5]
print(balancedSplitExists(a))

# F
a = [3, 6, 3, 4, 4]
print(balancedSplitExists(a))
