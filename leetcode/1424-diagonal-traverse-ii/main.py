from collections import defaultdict

"""
    1st: brute force
    TLE: some cells are missing, we dont need to calculate
    52 / 56 test cases passed.
"""


class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        maxCol = 0
        for col in nums:
            maxCol = max(maxCol, len(col))

        res = []
        for i in range(len(nums)):
            _i, j = i, 0
            while _i >= 0:
                if j < len(nums[_i]):
                    res.append(nums[_i][j])
                _i -= 1
                j += 1
        for j in range(1, maxCol):
            i, _j = len(nums)-1, j
            while i >= 0:
                if _j < len(nums[i]):
                    res.append(nums[i][_j])
                i -= 1
                _j += 1
        return res


"""
    2nd: sort
    - since some cells are missing, we dont need to traverse or the (i, j) is ROW * MAX_COL

    Time    O(R ClogC)
    Space   O(RC)
    1124 ms, faster than 72.52% 
"""


class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        maxCol = 0
        for col in nums:
            maxCol = max(maxCol, len(col))

        ht = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                k = i + j
                ht[k].append((i, j))

        for key in ht:
            ht[key].sort(reverse=True)

        res = []
        for total in range(len(nums) + maxCol):
            for i, j in ht[total]:
                res.append(nums[i][j])
        return res
