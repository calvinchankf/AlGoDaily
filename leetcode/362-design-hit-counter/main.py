from collections import Counter
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
        self.od = OrderedDict()

    def hit(self, timestamp):
        if timestamp in self.od:
            self.od[timestamp] += 1
        else:
            self.od[timestamp] = 1

    def getHits(self, timestamp):
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
        self.nums = []
        self.m = {}

    def hit(self, timestamp):
        if timestamp in self.m:
            self.m[timestamp] += 1
        else:
            self.nums.append(timestamp)
            self.m[timestamp] = 1

    def getHits(self, timestamp):
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


"""
    3rd: use Counter

    Time of hit()       O(1)
    Time of getHits()   O(1) cos it just counts 300 keys at maximum
    Space   O(n)
    28 ms, faster than 87.41%
"""


class HitCounter:

    def __init__(self):
        self.ht = Counter()

    def hit(self, timestamp: int) -> None:
        self.ht[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        res = 0
        toRemove = []
        for key in self.ht:
            if key > timestamp - 300:
                res += self.ht[key]
            else:
                toRemove.append(key)
        for x in toRemove:
            del self.ht[x]
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
