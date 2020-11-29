"""
    binary search
    a: actual energey
    m: minium energey
    - sort the array by (m-d, m)
    - binary search the result

    Time    O(NlogN + Nlog(2**32))
    Space   O(1)
    2504 ms, faster than 14.29%
"""


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1]-x[0], x[1]), reverse=True)
        left = 1
        right = 2**32
        while left < right:
            mid = (left + right)//2
            if self.canFinsih(tasks, mid):
                right = mid
            else:
                left = mid + 1
        return left

    def canFinsih(self, tasks, mid):
        for a, m in tasks:
            if mid >= m:
                mid -= a
            else:
                return False
        return True
