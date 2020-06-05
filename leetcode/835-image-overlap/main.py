"""
    1st: brute force + hashtable
    - put coordinates of 1 in a hashtable for both images
    - apply di, dj to check if there are overlaps

    Time    O(RRCC)
    Space   O(RC)
    2008 ms, faster than 5.93%
"""


class Solution:
    def largestOverlap(self, A, B):
        n = len(A)
        hsA = set()
        hsB = set()
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    hsA.add((i, j))
                if B[i][j] == 1:
                    hsB.add((i, j))
        maxOverlap = 0
        for di in range(-n, n):
            for dj in range(-n, n):
                overlap = self.checkOverlap(hsA, hsB, di, dj)
                maxOverlap = max(maxOverlap, overlap)
        return maxOverlap

    def checkOverlap(self, hsA, hsB, di, dj):
        res = 0
        for i, j in hsB:
            _i = i + di
            _j = j + dj
            if (_i, _j) in hsA:
                res += 1
        return res


s = Solution()

a = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
b = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]

print(s.largestOverlap(a, b))
