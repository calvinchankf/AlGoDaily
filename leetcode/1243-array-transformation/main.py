"""
    1st: array iteration
    - just loop the array and put the new values in a new array
    - do it until there is no more changes

    Time    O(kN)
    Space   O(N)
    20 ms, faster than 83.00%
"""


class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = arr[:]
        while True:
            isChanged = False
            temp = res[:]
            for i in range(1, len(arr)-1):
                if res[i] > res[i-1] and res[i] > res[i+1]:
                    temp[i] -= 1
                    isChanged = True
                elif res[i] < res[i-1] and res[i] < res[i+1]:
                    temp[i] += 1
                    isChanged = True
            res = temp
            if not isChanged:
                break
        return res
