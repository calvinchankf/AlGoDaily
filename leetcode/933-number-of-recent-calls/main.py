"""
    1st approach: queue
    - similar to lc362
    - remove the items (if x < t-3000) from the queue every time we enqueue new item

    Time of ping()      O(n)
    Space               O(n)
    316 ms, faster than 27.34%
"""


class RecentCounter(object):

    def __init__(self):
        self.arr = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.arr.append(t)
        while len(self.arr) > 0 and self.arr[0] < t-3000:
            self.arr.pop(0)
        return len(self.arr)

"""
    2nd: binary search

    Time of ping()      O(logN)
    Space               O(N)
    388 ms, faster than 34.59%
"""
class RecentCounter:

    def __init__(self):
        self.calls = []

    def ping(self, t: int) -> int:
        self.calls.append(t)
        j = self.lowerbsearch(self.calls, t - 3000)
        return len(self.calls) - j

        # it also works but the Time will be linear O(j)
        # self.calls = self.calls[j:]
        # return len(self.calls)
    
    def lowerbsearch(self, nums, t):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if t <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)