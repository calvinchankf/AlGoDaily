from collections import Counter

"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    44 ms, faster than 38.25%
"""


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ht = {}
        for i in range(len(arr)):
            ht[arr[i]] = i
        for i in range(len(arr)):
            target = arr[i] * 2
            if target in ht and ht[target] != i:
                return True
        return False


s = Solution()

a = [-766, 259, 203, 601, 896, -226, -844, 168, 126, -542, 159, -833, 950, -454, -253, 824, -395, 155, 94, 894, -766, -63, 836, -433, -780, 611, -
     907, 695, -395, -975, 256, 373, -971, -813, -154, -765, 691, 812, 617, -919, -616, -510, 608, 201, -138, -669, -764, -77, -658, 394, -506, -675, 523]
print(s.checkIfExist(a))

print("-----")

"""
    2nd: binary search
    Time    O(NlogN)
    Space   O(N)
    40 ms, faster than 61.30%
"""


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        pos, negs = [], []
        for x in arr:
            if x < 0:
                negs.append(-x)
            else:
                pos.append(x)

        pos = sorted(pos)
        if self.check(pos):
            return True
        negs = sorted(negs)
        if self.check(negs):
            return True

        return False

    def check(self, nums):
        nums = sorted(nums)
        for i in range(len(nums)):
            idx = self.bsearch(i+1, nums, nums[i] * 2)
            if idx != -1:
                return True

        return False

    def bsearch(self, start, nums, target):
        left = start
        right = len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1


s = Solution()
a = [-766, 259, 203, 601, 896, -226, -844, 168, 126, -542, 159, -833, 950, -454, -253, 824, -395, 155, 94, 894, -766, -63, 836, -433, -780, 611, -
     907, 695, -395, -975, 256, 373, -971, -813, -154, -765, 691, 812, 617, -919, -616, -510, 608, 201, -138, -669, -764, -77, -658, 394, -506, -675, 523]
print(s.checkIfExist(a))
