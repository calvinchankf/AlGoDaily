"""
    1st: math
    - learned from others 
    
    0. The hint: Find the smallest number from either rowSum or colSum, and let it be x, and subtract x from both rowSum and colSum
    1. res[i][j] will clear either row[i] or col[j], that means either row[i] == 0 and col[j] == 0 in the end
    2. It's guaranteed that at least one matrix that fulfills the requirements exists
    3. sum(row) == sum(col) always valid

    ref:
    - https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/discuss/876845/JavaC%2B%2BPython-Easy-and-Concise-with-Prove
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R = len(rowSum)
        C = len(colSum)
        res = [C * [0] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res