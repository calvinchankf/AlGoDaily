from collections import defaultdict
from random import choice

"""
    1st: hashtable
    - but the purpose of this question should be asking Reservoir Sampling, in a datastream instead of an array

    Time of init()  O(N)
    Time of pick()  O(1)
    Space           O(2N)
    312 ms, faster than 31.14% 
"""


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ht = defaultdict(list)
        for i in range(len(nums)):
            x = nums[i]
            self.ht[x].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        return choice(self.ht[target])


"""
    2nd: Reservoir Sampling

    Time of init()  O(1)
    Time of pick()  O(N)
    Space           O(N)
    244 ms, faster than 90.57%
"""


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = None
        count = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                # pick the current number with probability 1 / count (reservoir sampling)
                if random.randint(0, count) == 0:
                    res = i
                count += 1
        return res
