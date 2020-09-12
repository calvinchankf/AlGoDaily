import sys

"""
    https://leetcode.com/discuss/interview-question/480303/Amazon-or-Phone-or-K-weak-rows-in-a-matrix

    There are soldiers and civilians arranged in N x M matrix way, find out the 'K' weak rows in the matrix.
    Weak rows are those where numbers of soldiers are less compare to other siblings row.
    Soldiers are always stand in frontier, means always 1's may appear first and then 0's
    1 represents soldier
    0 represents civilian

    ex:
    K = 2
    matrix = [
        [1, 1, 1, 0, 0, 0]
        [1, 1, 0, 0, 0, 0]
        [1, 1, 1, 1, 0, 0]
        [1, 1, 0, 0, 0, 0]
    ]
    Here row 1 & 3 are weak rows since they have less numbers of 1's compare to row 0 & 2
"""


def findWeakRows(K, matrix):
    R = len(matrix)
    C = len(matrix[0])

    counts = []
    for i in range(R):
        j = upperBsearch(matrix[i])
        counts.append((j, i))
    counts.sort()

    res = []
    for i in range(min(K, len(counts))):
        count, idx = counts[i]
        res.append(idx)
    return res


def upperBsearch(nums):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if nums[mid] == 1:
            left = mid + 1
        else:
            right = mid
    return right


a = 2
b = [
    [1, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
]
print(findWeakRows(a, b))
