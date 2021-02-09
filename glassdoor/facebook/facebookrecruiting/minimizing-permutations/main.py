"""
    In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). 
    You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
    
    Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
    
    Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

    Example
    If N = 3, and P = (3, 1, 2), we can do the following operations:
    Select (1, 2) and reverse it: P = (3, 2, 1).
    Select (3, 2, 1) and reverse it: P = (1, 2, 3).
    output = 2
"""

"""
    brute force BFS
    - pretty sure that there is a better way but couldnt figure that out

    Time    O(N!) we try every permuation
    Space   O(N!)
"""


def minOperations(arr):
    n = len(arr)
    target = sorted(arr)
    targetKey = tuple(target)

    # BFS
    seen = set()
    start = tuple(arr)
    q = [(start, 0)]
    while len(q) > 0:
        key, steps = q.pop(0)

        if key == targetKey:
            return steps

        # any permutation will only been visited once
        if key in seen:
            continue
        seen.add(key)

        # swap every possible subarray
        nums = list(key)
        for i in range(n-1):
            for j in range(i+1, n):
                _nums = nums[:i] + nums[i:j+1][::-1] + nums[j+1:]
                _key = tuple(_nums)
                q.append((_key, steps + 1))
    return -1


a = [3, 1, 2]
print(minOperations(a))

a = [1, 2, 5, 4, 3]
print(minOperations(a))
