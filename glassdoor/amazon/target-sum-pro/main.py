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


def find4sumInArray(nums):
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
print(find4sumInArray(a))

a = [9, 3, 2, 1, 6, 6]
print(find4sumInArray(a))

print("----")

"""
    variation: find out all the triplets that a + b = c
"""


def find3sumInArray(nums):
    nums.sort()
    n = len(nums)
    ab = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            total = nums[i] + nums[j]
            ab[total].append((i, j))
    res = set()
    for i in range(n):
        if nums[i] in ab:
            pairs = ab[nums[i]]
            for a, b in pairs:
                hs = set([a, b, i])
                if len(hs) == 3:
                    res.add((nums[a], nums[b], nums[i]))
    return list(res)


a = [9, 3, 2, 1, 5]
print(find3sumInArray(a))

a = [9, 3, 2, 1, 5, 5]
print(find3sumInArray(a))

a = [8, 3, 2, 1, 5, 5]
print(find3sumInArray(a))

a = [0, 0, 0]
print(find3sumInArray(a))

a = [2, 2, 4, 4]
print(find3sumInArray(a))

a = [1, 0, 0, 1]
print(find3sumInArray(a))

print("-----")


def find3sumInArray(nums):
    nums.sort()
    n = len(nums)
    ht = defaultdict(list)
    for i in range(n):
        x = nums[i]
        ht[x].append(i)
    res = set()
    for i in range(n):
        for j in range(i+1, n):
            total = nums[i] + nums[j]
            if total in ht:
                if i in ht[total] and j in ht[total]:
                    if len(ht[total]) > 2:
                        triplet = (nums[i], nums[j], total)
                        res.add(triplet)
                elif i in ht[total] or j in ht[total]:
                    if len(ht[total]) > 1:
                        triplet = (nums[i], nums[j], total)
                        res.add(triplet)
                else:
                    triplet = (nums[i], nums[j], total)
                    res.add(triplet)
    return list(res)

a = [9, 3, 2, 1, 5]
print(find3sumInArray(a))

a = [9, 3, 2, 1, 5, 5]
print(find3sumInArray(a))

a = [8, 3, 2, 1, 5, 5]
print(find3sumInArray(a))

a = [0, 0, 0]
print(find3sumInArray(a))

a = [2, 2, 4, 4]
print(find3sumInArray(a))

a = [1, 0, 0, 1]
print(find3sumInArray(a))