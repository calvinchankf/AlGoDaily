import heapq


"""
    0th approach: brute-force sort

    Time    O(nlogn)
    Space   O(n)
    48 ms, faster than 73.06%
"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                arr.append(matrix[i][j])
        arr = sorted(arr)
        return arr[k-1]


a = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
print(Solution().kthSmallest(a, 8))

print("-----")


"""
    1st approach: max heap
    - use a max heap with limited capacity k
    - when we meet a new element and the heap overflows, 
    we pop the toppest element such that we can maintain the heap contains the k smallest elements only

    Time    O(RClogRC)
    Space   O(n)
    248 ms, faster than 14.97%
"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heapq.heappush(arr, -matrix[i][j])
                if len(arr) > k:
                    heapq.heappop(arr)
        return -arr[0]


a = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
print(Solution().kthSmallest(a, 8))

print("-----")


"""
    1st approach: min heap
    - similar to lc23, 373, 378

    Time    O(RlogR + KlogR)
    Space   O(RC)
    212 ms, faster than 44.46%
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        pq = []
        for row in matrix:
            first = row.pop(0)
            heapq.heappush(pq, (first, row))

        count = 1  # 1-based
        while len(pq) > 0:
            num, row = heapq.heappop(pq)
            if count == k:
                return num
            count += 1
            if len(row) > 0:
                first = row.pop(0)
                heapq.heappush(pq, (first, row))
        return None


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int

        suggested approach: binary search
        - start from left=first smallest number and right=largest number, and compute the mid point
        - for each row, calculate how many numbers <= mid point and adjust the mid point until we reach to a number where matrix[i][j] == kth

        e.g.
        nums = [
            [1,5,10]
            [9,10,13]
            [12,13,15]
        ]
        k = 6

        for each iteration:

        (1+15)/2=8, there are 2 numbers <= 6, so we assign left = 8+1 = 9
        (9+15)/2=12, there are 7 numbers ! <= 6, so we assign right = 12-1 = 11
        (9+11)/2=10, there are 5 numbers <= 6, so we assign left = 10+1 = 11
        (11+11)/2=11, there are 5 numbers <= 6, so we assign left = 11+1 = 12

        the loop exits, return left = 12

        ref:
        - https://www.hrwhisper.me/leetcode-kth-smallest-element-sorted-matrix/

        40 ms, faster than 82.78%
        """
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left <= right:
            mid = (left + right) / 2

            # for each row, binary search through itself to find the number of items which <= target
            count = 0
            for arr in matrix:
                x = self.upperboundBsearch(arr, mid)
                count += x

            # if count >= k, narrow down the scope to left and mid-1
            if count >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def upperboundBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) / 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


a = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
print(Solution().kthSmallest(a, 8))
