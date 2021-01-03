import heapq

"""
    https://leetcode.com/discuss/interview-question/570461/Facebook-or-Recruiting-Portal-or-Median-of-subarrays

    You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] (rounded down to the nearest integer).
    The median of a list of integers is defined as follows. If the integers were to be sorted, then:
    - If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
    - Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.

    Input: [5, 15, 1, 3]
    Output: [5, 10, 5, 4]

    Explanation:
    The median of [5] is 5, 
    the median of [5, 15] is (5 + 15) / 2 = 10, 
    the median of [5, 15, 1] is 5, 
    and the median of [5, 10, 1, 3] is (3 + 5) / 2 = 4.
"""

"""
    -> 1, 5 | 10, 22

    e.g.1
    1, 5 | 10, 22 <- 11
    1, 5 | 10, 11, 22 

    e.g.2
    1, 5 | 10, 22 <- 3
    1, 3 | 5, 10, 22 

    -> 1, 5 | 10, 11, 22 

    e.g.3
    1, 5 | 10, 11, 22 <- 100
"""


def findMedian(arr):
    maxheap = []  # left
    minheap = []  # right
    res = []
    for x in arr:
        if len(maxheap) == len(minheap):
            heappush(maxheap, -x)
            pop = -heappop(maxheap)
            heappush(minheap, pop)
        else:
            heappush(minheap, x)
            pop = heappop(minheap)
            heappush(maxheap, -pop)

        if len(maxheap) == len(minheap):
            left = -maxheap[0]
            right = minheap[0]
            res.append((left + right) // 2)
        else:
            res.append(minheap[0])
    return res


a = [5, 15, 1, 3]
print(medianOfSubarrays(a))

a = [1, 2]
print(medianOfSubarrays(a))

a = [2, 4, 7, 1, 5, 3]
print(medianOfSubarrays(a))
