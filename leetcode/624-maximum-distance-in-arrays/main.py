"""
    1st approach:
    - since we need to find the min/max from a different array, we need 2 variables to store the previous min and max
    
    e.g.               min max
    [
        [4,5],
        [1,2,3],        4   5
        [1,2,2],        1   5
        [-10,1],        1   5
    ]

    144 ms, faster than 38.16%
"""


class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res = 0
        prevMin = arrays[0][0]
        prevMax = arrays[0][-1]
        for i in range(1, len(arrays)):
            arr = arrays[i]
            # use current min and max to compute the distance
            curMin = arr[0]
            curMax = arr[-1]
            # see if there is max distance
            a = abs(curMin-prevMax)
            b = abs(curMax-prevMin)
            res = max(res, a, b)
            # update previous min and max
            prevMin = min(prevMin, curMin)
            prevMax = max(prevMax, curMax)
        return res

"""
    2nd: similar to 1st
    - but use indices to see if there is a index collision

    Time    O(N)
    Space   O(1)
    140 ms, faster than 100.00%
"""
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minNum1 = sys.maxsize
        minNum2 = sys.maxsize
        minIdx = -1
        
        maxNum1 = -sys.maxsize
        maxNum2 = -sys.maxsize
        maxIdx = -1
        
        for i in range(len(arrays)):
            nums = arrays[i]
            if nums[0] < minNum1:
                minNum2 = minNum1
                minNum1 = nums[0]
                minIdx = i
            elif nums[0] < minNum2:
                minNum2 = nums[0]
            
            if nums[-1] > maxNum1:
                maxNum2 = maxNum1
                maxNum1 = nums[-1]
                maxIdx = i
            elif nums[-1] > maxNum2:
                maxNum2 = nums[-1]
        
        if minIdx != maxIdx:
            return maxNum1 - minNum1
        return max(maxNum1-minNum2, maxNum2-minNum1)