"""
    1st: hashtable + sort

    Time    O(NlogN)
    Space   O(N)
    856 ms, faster than 33.33%
"""
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        numSet = set()
        for x, y in points:
            numSet.add(x)
        nums = sorted(list(numSet))
        maxDiff = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            maxDiff = max(maxDiff, diff)
        return maxDiff