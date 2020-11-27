"""
    1st: pointer

    Time of init()      O(N)
    Time of insert()    O(N)
    Space               O(N)
    204 ms, faster than 49.66%
"""


class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.ptr = 1
        self.nums = (n+1) * [None]

    def insert(self, oId, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        res = []
        self.nums[oId] = value
        i = self.ptr
        while i < len(self.nums):
            if self.nums[i] == None:
                break
            res.append(self.nums[i])
            i += 1
        self.ptr = i
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
