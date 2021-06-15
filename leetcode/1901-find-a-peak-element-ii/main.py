"""
    1st: binary search
    - on every row, binary search a local maximal
    - reuse lc162

    Time    O(RlogC)
    Space   O(1)
    1220 ms, faster than 100.00%
"""


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        R, C = len(mat), len(mat[0])
        mat.insert(0, C * [-1])
        mat.append(C * [-1])
        for i in range(1, R+1):
            j = self.findPeakElement(mat[i])
            if mat[i][j] > mat[i-1][j] and mat[i][j] > mat[i+1][j]:
                return [i-1, j]
        return [-1, -1]

    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
