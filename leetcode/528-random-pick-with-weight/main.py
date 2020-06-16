from typing import List
import random

"""
    1st: binary search
    e.g. [1,5,2]

    Prefix-sum array: [1,6,8]

    Consider any number from 1 to 8, we should get 
    [1,2,3,4,5,6,7,8]
    [0,1,1,1,1,1,1,2] <- we should always get 1 when we search from 2 to 7 inclusive

    Clearly, we can do it with a binary search to find number that >= target

    Time of init()          O()
    Time of pickIndex()     O(logN)
    Space                   O(N)
    316ms beats 40.72%
"""


class Solution:

    def __init__(self, w: List[int]):
        self.nums = []
        pfs = 0
        for x in w:
            pfs += x
            self.nums.append(pfs)

    def pickIndex(self) -> int:
        r = random.randrange(1, self.nums[-1] + 1)
        return self.bsearch(self.nums, r)

    def bsearch(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        # to find number that >= target
        return left
