"""
    1st: prefix sum + hashtable
    - calculate the prefix sum for each row
    - for every pair of columns, calculate the accumulated sum of rows
    - this is exactly what we do lc506 vertically

    ref:
    - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/303750/JavaC%2B%2BPython-Find-the-Subarray-with-Target-Sum

    Time    O(RCC)
    Space   O(RC)
    836 ms, faster than 77.18%
"""


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix or not matrix[0]:
            return
        R, C = len(matrix), len(matrix[0])
        rows = [C*[0] for _ in range(R)]
        for i in range(R):
            pfs = 0
            for j in range(C):
                pfs += matrix[i][j]
                rows[i][j] = pfs
        total = 0
        for j1 in range(C):
            for j2 in range(j1, C):
                # lc506: Subarrays Sum Equals K
                ht = {}
                pfs = 0
                for i in range(R):
                    x = rows[i][j2] - (rows[i][j1-1] if j1 > 0 else 0)
                    pfs += x
                    if pfs == target:
                        total += 1
                    remain = pfs - target
                    if remain in ht:
                        total += ht[remain]
                    if pfs not in ht:
                        ht[pfs] = 0
                    ht[pfs] += 1

        return total
