
import heapq

"""
    1st: binary search + heapq
    - we just care about the possible diffs
    - we use bricks to climb the smaller diffs first
    - we use ladder to climb the bigger diffs afterwards

    Time    O(NlogN)
    Space   O(N)
    5388 ms, faster than 5.22%
"""
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        left = 0
        right = len(heights)
        while left < right:
            mid = (left + right)//2
            diffs = self.getDiffs(heights, mid)
            heapq.heapify(diffs)
            if self.canReach(bricks, ladders, diffs):
                left = mid + 1
            else:
                right = mid
        return left - 1
            
    
    def canReach(self, bricks, ladders, diffs):
        _bricks = bricks
        _ladders = ladders
        while len(diffs) > 0:
            pop = heapq.heappop(diffs)
            if _bricks >= pop:
                _bricks -= pop
            elif _ladders > 0:
                _ladders -= 1
            else:
                return False
        return True
    
    def getDiffs(self, heights, k):
        diffs = []
        for i in range(1, k+1):
            if heights[i] - heights[i-1] > 0:
                diffs.append(heights[i] - heights[i-1])
        return diffs