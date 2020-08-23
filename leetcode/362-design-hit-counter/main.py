from collections import *

"""
    1st approach:
    - dictionary + array(perserves the order) <= there is a handy class in python, OrderedDict, does the same thing
    - hit() => put the keys in the orderdict, increment the count for existing keys
    - getHits() => count the result by iterating through the OrderedDict from back until the key <= timestamp - 300

    Time: hit()       O(1)
    Time: getHits()   O(1) cos it just counts 300 keys at maximum
    Space   O(n)
    16 ms, faster than 100.00%
"""


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.od = OrderedDict()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if timestamp in self.od:
            self.od[timestamp] += 1
        else:
            self.od[timestamp] = 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        items = self.od.items()
        n = len(items)
        for i in range(n-1, -1, -1):
            key, cnt = items[i]
            if key > timestamp - 300:
                res += cnt
            else:
                del od[key]
        return res


"""
    2nd approach:
    - dont use OrderedDict, use a hashtable + array to do the same thing
    - hit() => put the keys in the hashtable, increment the count for existing keys
    - getHits() => count the result by iterating through the hashtable from back until the key <= timestamp - 300

    Time of hit()       O(1)
    Time of getHits()   O(1) cos it just counts 300 keys at maximum
    Space   O(n)
    16 ms, faster than 100.00%
"""


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.m = {}

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        if timestamp in self.m:
            self.m[timestamp] += 1
        else:
            self.nums.append(timestamp)
            self.m[timestamp] = 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        j = -1
        for i in range(len(self.nums)-1, -1, -1):
            key = self.nums[i]
            cnt = self.m[key]
            if key > timestamp - 300:
                res += cnt
            else:
                del self.m[key]
                # set the index for removing
                if j == -1:
                    j = i
        self.nums = self.nums[j+1:]
        return res
