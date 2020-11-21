"""
    1st approach: similar to 2 pointers
    - maintain 2 arrays which represent 2 sides of a mountain
    - when arr[i] > arr[i-1], append left
    - when arr[i] < arr[i-1], append right
    - when arr[i] == arr[i-1], reset the left and right
    - need to take care of the pivot point, e.g. 3,4,5,2,1,x. When x is > arr[i-1] and x > right[-1], reset the left and right

    Time    O(N)
    Space   O(N)
    164 ms, faster than 24.55%
"""


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        forward = n * [1]
        for i in range(1, n):
            if A[i] > A[i-1]:
                forward[i] = forward[i-1] + 1
        backward = n * [1]
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                backward[i] = backward[i+1] + 1
        res = 0
        for i in range(n):
            if forward[i] > 1 and backward[i] > 1:
                res = max(res, forward[i] + backward[i] - 1)
        return res
