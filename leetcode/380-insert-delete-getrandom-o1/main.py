import random

"""
    1st: hashtable
    - straight forward approach

    Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		    O(N)
	Space					O(n) the unique keys
    256 ms, faster than 29.35% 
"""


class RandomizedSet(object):

    def __init__(self):
        self.ht = {}

    def insert(self, val):
        if val in self.ht:
            return False
        self.ht[val] = True
        return True

    def remove(self, val):
        if val not in self.ht:
            return False
        del self.ht[val]
        return True

    def getRandom(self):
        idx = random.randint(0, len(self.ht)-1)
        nums = self.ht.keys()
        return nums[idx]


"""
	2nd approach: hashtable + array, learned from others
	- save value: index in hashtable
	- when delete, swap the target item and the last item in the array, and remove the last item
	- see ./idea_add.png and ./idea_remove.png

	Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		    O(1)
	Space					O(n) the unique keys
	92 ms, faster than 78.93%
"""


class RandomizedSet(object):

    def __init__(self):
        self.ht = {}
        self.nums = []

    def insert(self, val):
        if val in self.ht:
            return False
        self.ht[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val not in self.ht:
            return False
        idx = self.ht[val]
        last = self.nums[-1]
        self.ht[last] = idx
        self.nums[idx] = last
        self.nums.pop()
        del self.ht[val]
        return True

    def getRandom(self):
        idx = random.randint(0, len(self.nums)-1)
        return self.nums[idx]
