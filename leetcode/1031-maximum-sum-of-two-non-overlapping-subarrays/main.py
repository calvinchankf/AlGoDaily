from typing import List

"""
    1st: prefix sum
    - calculate any subarray sum at each index
    - for each L length subarray, find the best possible M length subarray that occurs before and after it

    Time    O(N^2)
    Space   O(N)
    316 ms, faster than 17.03%
"""


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        N = len(A)
        prefixSums = []
        total = 0
        for i in range(N):
            total += A[i]
            prefixSums.append(total)
        res = 0
        for i in range(L-1, N):
            window_l = prefixSums[i] - (prefixSums[i-L] if i-L >= 0 else 0)
            for j in range(M-1, i-L+1):
                window_m = prefixSums[j] - (prefixSums[j-M] if j-M >= 0 else 0)
                res = max(res, window_l + window_m)
            for j in range(i+M, N):
                window_m = prefixSums[j] - (prefixSums[j-M] if j-M >= 0 else 0)
                res = max(res, window_l + window_m)
        return res


s = Solution()

a = [0, 6, 5, 2, 2, 5, 1, 9, 4]
b = 1
c = 2
print(s.maxSumTwoNoOverlap(a, b, c))

a = [3, 8, 1, 3, 2, 1, 8, 9, 0]
b = 3
c = 2
print(s.maxSumTwoNoOverlap(a, b, c))

a = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
b = 4
c = 3
print(s.maxSumTwoNoOverlap(a, b, c))
