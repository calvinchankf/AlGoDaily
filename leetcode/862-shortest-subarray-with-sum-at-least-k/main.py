from heapq import *

"""
    1st: minheap
    - calculate prefix sum at every index
    - at every index, subtract the min prefix sum from the left, so that we can have a short subarray in between

    e.g. [1, 1, 1, 5, -2, -3, 4, 3, 6]
    pfs   1  2  3  8   6   3  7 10 16

    imagine you keep a minheap, we can keep popping the leftmost prefixSum, 
    so that would come up with a shorter subarray in between

    1  2  3  8   6   3  7 10 16
             ^ minheap = [1,2,3], we can pop the 1
    
    1  2  3  8   6   3  7 10 16
                           ^ [2,3,3,6,7,8,10], we will pop the first 3 items
                                  ^
                                and this, prefixSum=3 at index=5, is what we want

    ref:
    - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/531032/3-Clean-Python-Solution%3A-Deque-Heap-or-Binary-Search

    Time    O(NlogN)
    Space   O(N)
    972 ms, faster than 12.16%
"""


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        minheap = []
        pfs = 0
        res = 2**32
        for i in range(len(A)):
            x = A[i]
            pfs += x
            if pfs >= K:
                res = min(res, i+1)
            while len(minheap) > 0 and pfs - minheap[0][0] >= K:
                _pfs, j = heappop(minheap)
                res = min(res, i - j)
            heappush(minheap, (pfs, i))
        if res == 2**32:
            return -1
        return res


"""
    2nd: dequeue
    - calculate prefix sum at every index
    - while prefixSum[i] - q[0][0] >= K, subtract the dequeue from the left
    - while prefixSum[i] <= q[-1][0], pop q[-1] and add prefixSum[i] to the queue.
    *** The reason is, if the current prefixSum[i] is smaller than q[-1][0], 
    *** then prefixSum[future] can just subtract prefixSum[i] to get a shorter subarray
    
    e.g. [1, 1, 1, 5, -2, -3, 4, 3, 6]
    pfs   1  2  3  8   6   3  7 10 16
    idx   0  1  2  3   4   5  6  7 8

    deq []
        [(0, 0)]
        [(0, 0), (1, 1)]
        [(0, 0), (1, 1), (2, 2)]
        [(0, 0), (1, 1), (2, 2), (3, 3)]
        [(2, 2), (3, 3), (8, 4)]
        [(2, 2), (3, 3), (6, 5)]
        [(2, 2), (3, 6)]
        [(2, 2), (3, 6), (7, 7)]
        [(7, 7), (10, 8)]                   <- final result = 8 - 6 = 2
        [(10, 8), (16, 9)]

    ref:
    - https://www.cnblogs.com/grandyang/p/11300071.html

    Time    O(N)
    Space   O(N)
    988 ms, faster than 10.46%
"""


class Solution(object):
    def shortestSubarray(self, A, K):
        n = len(A)
        # prefix sum
        pfs = 0
        pfss = [0]
        for i in range(n):
            pfs += A[i]
            pfss.append(pfs)
        # dequeue
        res = 2**32
        q = []  # [(pfs, idx), ...]
        for i in range(n+1):
            while len(q) > 0 and pfss[i] - q[0][0] >= K:
                _pfs, j = q.pop(0)
                res = min(res, i - j)
            while len(q) > 0 and pfss[i] <= q[-1][0]:
                q.pop()
            q.append((pfss[i], i))
        if res == 2**32:
            return -1
        return res
