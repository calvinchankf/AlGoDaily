from heapq import *

"""
    1st: prefix XOR sum + minheap
    
    Time    O(RC logK)
    Space   O(K)
    3756 ms, faster than 33.33%
"""


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        minheap = []
        for i in range(R):
            pfs = 0
            for j in range(C):
                pfs ^= matrix[i][j]
                if i == 0:
                    matrix[i][j] = pfs
                else:
                    matrix[i][j] = pfs ^ matrix[i-1][j]
                heappush(minheap, matrix[i][j])
                if len(minheap) > k:
                    heappop(minheap)
        return minheap[0]
