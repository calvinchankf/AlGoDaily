"""
    1st: binary search

    Time    O(NlogR) N:length of the array, R: max number in the array
    Space   O(1)
    140 ms, faster than 36.25%
"""


class Solution(object):
    def findBestValue(self, arr, target):
        left = 1
        right = max(arr)
        while left <= right:
            mid = (left + right)//2
            total = self.calculate(arr, mid)
            if target < total:
                right = mid - 1
            elif target > total:
                left = mid + 1
            else:
                return mid
        a = self.calculate(arr, left)
        b = self.calculate(arr, right)
        if abs(a - target) < abs(b - target):
            return left
        return right

    def calculate(self, arr, threshold):
        total = 0
        for i in range(len(arr)):
            if arr[i] > threshold:
                total += threshold
            else:
                total += arr[i]
        return total
