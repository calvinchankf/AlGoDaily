from collections import *

"""
    1st: hashtable table
    - it is basically a 2sum, but mutable

    Time of init()      O(B)
    Time of add()       O(1)
    Time of count()     O(A)
    1052 ms, faster than 58.82%
"""


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.ht = Counter()
        for i in range(len(nums2)):
            x = nums2[i]
            self.ht[x] += 1

    def add(self, index: int, val: int) -> None:
        origX = self.nums2[index]
        newX = origX + val
        self.nums2[index] = newX

        self.ht[origX] -= 1
        self.ht[newX] += 1

    def count(self, tot: int) -> int:
        count = 0
        for x in self.nums1:
            remain = tot - x
            if remain in self.ht:
                count += self.ht[remain]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
