"""
    1st: subarray

    Time    O(MN)
    Space   O(N)
    28 ms, faster than 90.70%
"""


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        n = len(index)
        for i in range(n):
            idx = index[i]
            num = nums[i]
            res = res[:idx] + [num] + res[idx:]
        return res


"""
    2nd: same logic but different using a diff array emthod

    Time    O(MN)
    Space   O(N)
    28 ms, faster than 90.70%
"""


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        n = len(index)
        for i in range(n):
            idx = index[i]
            num = nums[i]
            res.insert(idx, num)
        return res
