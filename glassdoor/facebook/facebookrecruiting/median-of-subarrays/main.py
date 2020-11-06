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
def medianOfSubarrays(nums):
    maxHeap = []
    minHeap = []
    res = []
    for i in range(len(nums)):
        x = nums[i]
        if len(maxHeap) == len(minHeap):
            heapq.heappush(maxHeap, -x)
            maxFromLeft = -(heapq.heappop(maxHeap))
            heapq.heappush(minHeap, maxFromLeft)
        else:
            heapq.heappush(minHeap, x)
            minFromRight = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -minFromRight)
        
        if i%2 == 0:
            res.append(minHeap[0])
        else:
            a = maxHeap[0]
            b = minHeap[0]
            c = int((-a + b) / 2.0)
            res.append(c)
    return res

a = [5, 15, 1, 3]
print(medianOfSubarrays(a))