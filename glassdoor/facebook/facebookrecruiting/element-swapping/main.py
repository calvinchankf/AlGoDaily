"""
    Given a sequence of n integers arr, 
    determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps, 
    each involving a pair of consecutive elements in the sequence.

    Note: A list x is lexicographically smaller than a different equal-length list y if and only if, 
    for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.

    Example 1
    n = 3
    k = 2
    arr = [5, 3, 1]
    output = [1, 5, 3]
    We can swap the 2nd and 3rd elements, followed by the 1st and 2nd elements, to end up with the sequence [1, 5, 3]. This is the lexicographically smallest sequence achievable after at most 2 swaps.
    
    Example 2
    n = 5
    k = 3
    arr = [8, 9, 11, 2, 1]
    output = [2, 8, 9, 11, 1]
    We can swap [11, 2], followed by [9, 2], then [8, 2].
"""

"""
    Not sure if it is correct!

    Approach: 
    - find the i where the numbr has the maxDiff with the number on the left
    - perform swapping

    Time    O(N)
    Space   O(1)
"""


def findMinArray(arr, k):
    n = len(arr)
    maxDiff = 0
    target = -1
    for i in range(1, n):
        diff = arr[i-1] - arr[i]
        if diff >= maxDiff:
            maxDiff = diff
            target = i
    while k > 0 and target-1 >= 0:
        arr[target], arr[target-1] = arr[target-1], arr[target]
        target -= 1
        k -= 1
    return arr
