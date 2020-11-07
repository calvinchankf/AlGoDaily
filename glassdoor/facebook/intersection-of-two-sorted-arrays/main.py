"""
    This is a followup question of lc349

    try to solve it under these constraints:
    - O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
    - You are told the lists are sorted.

    e.g.
    [1, 5, 7, 7, 11]
    [2, 3, 5, 5, 7, 7, 10]

    result: [5, 7]

    Cases to take into consideration include: duplicates, negative values, single value lists, 0's, and empty list arguments.
    Other considerations might include sparse arrays.
"""
def findIntersections(nums1, nums2):

    # given that they are sorted already
    # nums1.sort()
    # nums2.sort()

    i, j = 0, 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.append(nums1[i]) # or nums2[j]
            while i + 1 < len(nums1) and nums1[i] == nums1[i+1]:
                i += 1
            i += 1
            while j + 1 < len(nums2) and nums2[j] == nums2[j+1]:
                j += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return res 

a = [1, 5, 7, 7, 11]
b = [2, 3, 5, 5, 7, 7, 10]
print(findIntersections(a, b)) # [5, 7]

print("-----")

"""
    if to include duplicates

    e.g.
    [1, 5, 7, 7, 11]
    [2, 3, 5, 5, 7, 7, 10]

    result: [5, 7, 7]
"""
def findIntersections(nums1, nums2):

    # given that they are sorted already
    # nums1.sort()
    # nums2.sort()

    i, j = 0, 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            cur = nums1[i]
            
            count1 = 1
            while i + 1 < len(nums1) and nums1[i] == nums1[i+1]:
                i += 1
                count1 += 1
            i += 1
            count2 = 1
            while j + 1 < len(nums2) and nums2[j] == nums2[j+1]:
                j += 1
                count2 += 1
            j += 1

            res += min(count1, count2) * [cur]

        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return res 

a = [1, 5, 7, 7, 11]
b = [2, 3, 5, 5, 7, 7, 10]
print(findIntersections(a, b)) # [5, 7]