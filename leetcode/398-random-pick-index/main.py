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
        targetIndexCount = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                targetIndexCount += 1
                # randomly pick from 1 to count, so the current number would have 1/count probability
                if random.randint(1, targetIndexCount) == 1:
                    res = i
        return res
