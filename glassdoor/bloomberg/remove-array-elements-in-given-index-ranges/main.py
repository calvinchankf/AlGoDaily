"""
    Input: array = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76], ranges = [[5, 8], [10, 13], [3, 6], [20, 25]]
    Output: [-8, 3, -5, 29, 43, 76, 73, 76]
"""


def removeItems(nums, ranges):
    """
        merge intervals + binary search

         0   1  2   3  4   5   6   7   8   9  10  11  12  13  14  15
        [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
                    ^
                    binary search
    """
    intvs = mergeIntervals(ranges)
    res = []
    for i in range(len(nums)):
        x = nums[i]
        j = bsearch(intvs, i)
        if 0 <= j < len(intvs):
            s, e = intvs[j]
            if s <= i <= e:
                continue
        res.append(x)
    return res


def mergeIntervals(intvs):
    res = []
    intvs.sort()
    for s, e in intvs:
        if len(res) == 0:
            res.append([s, e])
        else:
            if s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
    return res


def bsearch(intvs, target):
    left = 0
    right = len(intvs)-1
    while left <= right:
        mid = (left + right)//2
        if target < intvs[mid][0]:
            right = mid - 1
        elif target > intvs[mid][0]:
            left = mid + 1
        else:
            return mid
    # to find number that <= target
    return right


a = [-8, 3, -5, 1, 51, 56, 0, -5, 29, 43, 78, 75, 32, 76, 73, 76]
b = [[5, 8], [10, 13], [3, 6], [20, 25]]
print(removeItems(a, b))
