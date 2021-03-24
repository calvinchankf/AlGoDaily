"""
    1st: sort
    
    Time    O(N^2)
    Space   O(N)
    96 ms, faster than 68.00%
"""


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        t = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count += 1
            t.append((count, i))
        t.sort()
        return [x[1] for x in t[:k]]


"""
    2nd: upper binary search
    
    Time    O(RlogC)
    Space   O(1)
    100 ms, faster than 58.63%
"""


class Solution(object):
    def kWeakestRows(self, matrix, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        R = len(matrix)
        C = len(matrix[0])

        counts = []
        for i in range(R):
            j = self.upperBsearch(matrix[i])
            counts.append((j, i))
        counts.sort()

        res = []
        for i in range(min(k, len(counts))):
            count, idx = counts[i]
            res.append(idx)
        return res

    def upperBsearch(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] == 1:
                left = mid + 1
            else:
                right = mid
        return right


"""
    3rd: lower binary search
    
    Time    O(RlogC)
    Space   O(1)
    100 ms, faster than 58.63%
"""


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = []
        for i in range(len(mat)):
            row = mat[i]
            count = self.bsearch(row)
            counts.append((count, i))
        counts.sort()
        res = []
        for count, i in counts:
            res.append(i)
            if len(res) == k:
                break
        return res

    def bsearch(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == 0:
                right = mid
            else:
                left = mid + 1
        return left
