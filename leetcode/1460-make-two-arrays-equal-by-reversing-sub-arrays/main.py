"""
    1st: sort
    - sort the two arrays and check if they are equal

    Time    O(NlogN + MlogM)
    Space   O(1)
    88 ms, faster than 100.00%
"""


class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        target.sort()
        arr.sort()
        for i in range(len(arr)):
            if target[i] != arr[i]:
                return False
        return True
