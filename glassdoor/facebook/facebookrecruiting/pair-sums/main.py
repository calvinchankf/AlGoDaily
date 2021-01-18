from collections import Counter

"""
    Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.

    If an integer appears in the list multiple times, each copy is considered to be different; that is, 
    two pairs are considered different if one pair includes at least one array index which the other doesn't, 
    even if they include the same values.

    Example 1
    arr = [1, 2, 3, 4, 3]
    k = 6
    output = 2
    The valid pairs are 2+4 and 3+3.
    
    Example 2
    arr = [1, 5, 3, 3, 3]
    k = 6
    output = 4
    There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
"""


def numberOfWays(arr, k):
    ht = Counter(arr)
    res = 0
    for x in arr:
        remain = k - x
        if remain in ht:
            if remain == x:
                res += ht[remain] - 1
            else:
                res += ht[remain]
    return res/2
