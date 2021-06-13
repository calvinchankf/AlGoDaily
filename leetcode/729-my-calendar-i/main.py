"""
    1st approach: binary search

    there are 2 cases in a lower bound binary search

    e.g.1
    arr = [2,4,6,6,6,8,10], target=6
    return 2

    e.g.2
    arr = [2,4,6,6,6,8,10], target=5
    return 2

    therefore we can just use lower bound to look for the interval that which start time is >= book(start, end), 
    and such that the intvs[idx-1] must be the interval that earlier than the book(start, end)

    we can just compare the start and end between them

    Time    O(logn) for each book()
    Space   O(n)
    240 ms, faster than 78.91%
"""


class MyCalendar(object):

    def __init__(self):
        self.intvs = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        idx = self.lowerBsearch(self.intvs, start)
        if idx > 0 and self.intvs[idx-1][1] > start:
            return False
        if idx < len(self.intvs) and end > self.intvs[idx][0]:
            return False
        self.intvs.insert(idx, [start, end])
        return True

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid][0]:
                right = mid
            else:
                left = mid + 1
        return left
