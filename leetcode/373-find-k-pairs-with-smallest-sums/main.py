"""
    1st: brute force sort

	Time 	O(AB logAB)
	Space	O(MN)
	260 ms, faster than 34.73%
"""


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        arr = []
        for x in nums1:
            for y in nums2:
                arr.append((x + y, x, y))
        arr.sort()
        arr = arr[:k]
        res = []
        for i in range(len(arr)):
            s, x, y = arr[i]
            res.append([x, y])
        return res


"""
    2nd: min heap, learned from others
    - same logic as 786
    - similar to lc23, 373, 378, 786
    - since the arrays are sorted, we dont have to consider all pairs
    we can just care if we can pop k smallest items out from the stack
    
    e.g.
    a = [1, 3, 11]
    b = [2, 4, 6]
    k = 4

    heap = [1+2, 3+2, 11+2], consider the total of every element of nums1 + nums2[0]
    
    heap = [3, 5, 13]
    
    count = 0, we pop the first one because it must be smallest one,
    3 (i=0, j=0) = heap.pop()
    heap = [5, 11]
    then we consider adding nums1[0] + nums2[0+1 = 1] = 1 + 4 = 5 to the heap
    heap = [5, 5, 13]
    
    count = 1, we pop the first one because it must be smallest one,
    5 (i=0, j=1) = heap.pop()
    heap = [5, 13]
    then we consider adding nums1[0] + nums2[1+1] = 1 + 6 = 7 to the heap
    heap = [5, 7, 13]

    count = 2, we pop the first one because it must be smallest one,
    5 (i=1, j=0) = heap.pop()
    heap = [7, 13]
    then we consider adding nums1[1] + nums2[0+1] = 3 + 4 = 7 to the heap
    heap = [7, 7, 13]

    count = 3 we pop the first one because it must be smallest one,
    7 (i=0, j=2) = heap.pop()
    since count + 1 == k, we are done!!! 7 is the 4th smallest pairsum

    ref:
    - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84550/Slow-1-liner-to-Fast-solutions
    - https://www.youtube.com/watch?v=APZbA_q1zAc

	Time 	O(A + klogA)
	Space	O(MN)
	36 ms, faster than 86.84%
"""


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if len(nums1) == 0 or len(nums2) == 0 or k == 0:
            return []
        pq = []
        for i in range(len(nums1)):
            x = nums1[i]
            y = nums2[0]
            heapq.heappush(pq, (x+y, i, 0))
        res = []
        while len(pq) > 0:
            _, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])
            if len(res) == k:
                break
            if j + 1 < len(nums2):
                x = nums1[i]
                y = nums2[j+1]
                heapq.heappush(pq, (x+y, i, j+1))
        return res
