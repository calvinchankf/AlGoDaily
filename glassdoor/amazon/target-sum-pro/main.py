from collections import defaultdict

"""
    Question:
    - https://leetcode.com/discuss/interview-question/763964/Amazon-or-Phone-or-Target-Sum-Pro

    Problem:
    Given an unsorted list of integers, 
    return all combinations of 4 integers such that a + b + c = z where a, b, c, and z are all integers in the given list. 
    Each element of the list may only be used once in each combination. 
    Note: The interviewer discouraged sorting the inputted list.

    Example:

    Input: [9, 3, 2, 1, 6]
    Output: [1, 2, 3, 6], [1, 2, 6, 9]
"""


def find3sumInArray(nums):
    n = len(nums)
    ab = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            total = nums[i] + nums[j]
            ab[total].append((i, j))
    ht = {}
    for i in range(n):
        for j in range(i+1, n):
            total = abs(nums[i] - nums[j])
            if total in ab:
                for aIdx, bIdx in ab[total]:
                    s = [aIdx, bIdx, i, j]
                    if len(s) == 4:
                        s.sort()
                        key = tuple(s)
                        ht[key] = sorted([nums[x] for x in s])
    res = []
    for key in ht:
        res.append(ht[key])
    return res


a = [9, 3, 2, 1, 6]
print(find3sumInArray(a))

a = [9, 3, 2, 1, 6, 6]
print(find3sumInArray(a))
