from collections import Counter
"""
    Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
    
    Signature
    bool areTheyEqual(int[] arr_a, int[] arr_b)
    
    Input
    All integers in array are in the range [0, 1,000,000,000].
    
    Output
    Return true if B can be made equal to A, return false otherwise.
    
    Example
    A = [1, 2, 3, 4]
    B = [1, 4, 3, 2]
    output = true
    After reversing the subarray of B from indices 1 to 3, array B will equal array A.
"""


def are_they_equal(array_a, array_b):
    counterA = Counter(array_a)
    counterB = Counter(array_b)
    keys = set(list(counterA.keys()) + list(counterB.keys()))
    for k in keys:
        if k not in counterA or k not in counterB:
            return False
        if counterA[k] != counterB[k]:
            return False
    return True


a = [1, 2, 3, 4]
b = [1, 4, 3, 2]
print(are_they_equal(a, b))

a = [1, 2, 3, 4]
b = [1, 2, 3, 5]
print(are_they_equal(a, b))

a = [1, 2, 3, 4]
b = [2, 1, 4, 3]
print(are_they_equal(a, b))
