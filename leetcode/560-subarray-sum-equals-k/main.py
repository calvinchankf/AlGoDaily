from collections import *
"""
    1st approach: zero sum subarray
    - this question is fucking similar to leetcode 325, 525, 930, 1124, 1171, 1546
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: number of occurence of a previous sum
    - if currentSum - target in the hastable, the result += occurence

    e.g. [1, -1, 5, -2, 1, 2], 3
    when it comes to 2, remain = 6 - 3 = 3 and 3 is in the hashtable what does it mean?

    consider that a = [1,-1,5,-2] = 3,  b = [1, -1, 5, -2, 1, 2] = 6, 
    6-3 means the remain from a - b, which is [1,2], is = target k
    
    ref:
    - https://www.youtube.com/watch?v=hLcYp67wCcM

    Time	O(n)
    Space O(n)
    36ms beats 96.05%
    28jan2019
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        pfs = 0
        # key: previous sum, value: number of occurence of a previous sum
        ht = {}
        for i in range(len(nums)):
            pfs += nums[i]
            # if pfs == k, it is one of the target subarray
            if pfs == k:
                res += 1
            # if pfs-k in hashtable, it is one of the target subarray
            remain = pfs-k
            if remain in ht:
                res += ht[remain]
            # put the pfs into the hashtable
            if pfs not in ht:
                ht[pfs] = 1
            else:
                ht[pfs] += 1
        return res


print(Solution().subarraySum([1, 1, 1], 1))  # 3
print(Solution().subarraySum([1, 1, 1], 2))  # 2
print(Solution().subarraySum([1, 1, 1], 3))  # 1
print(Solution().subarraySum([1, 1, 1, 1], 3))  # 2
print(Solution().subarraySum([1, -1, 5, -2, 3], 3))  # 3
print(Solution().subarraySum([1, -1, 5, -2, 1, 2], 3))  # 4
print(Solution().subarraySum([-2, -1, 2, 1], 1))  # 2
print(Solution().subarraySum([-2, -1, 2, 1, 100], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 100, 1], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 1000], 99))  # 0

print("-----")

"""
    same approach but defaultdict

    Time	O(n)
    Space   O(n)
    100 ms, faster than 58.81%
    7jul2019
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        pfs = 0
        # key: previous sum, value: number of occurence of a previous sum
        ht = defaultdict(int)
        for i in range(len(nums)):
            pfs += nums[i]
            # if pfs == k, it is one of the target subarray
            if pfs == k:
                res += 1
            # if pfs-k in hashtable, it is one of the target subarray
            remain = pfs-k
            if remain in ht:
                res += ht[remain]
            # put the pfs into the hashtable
            ht[pfs] += 1
        return res


print(Solution().subarraySum([1, 1, 1], 1))  # 3
print(Solution().subarraySum([1, 1, 1], 2))  # 2
print(Solution().subarraySum([1, 1, 1], 3))  # 1
print(Solution().subarraySum([1, 1, 1, 1], 3))  # 2
print(Solution().subarraySum([1, -1, 5, -2, 3], 3))  # 3
print(Solution().subarraySum([1, -1, 5, -2, 1, 2], 3))  # 4
print(Solution().subarraySum([-2, -1, 2, 1], 1))  # 2
print(Solution().subarraySum([-2, -1, 2, 1, 100], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 100, 1], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 1000], 99))  # 0

print("-----")


"""
    followup: list the intervals
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = []
        pfs = 0
        # key: previous sum, value: number of occurence of a previous sum
        ht = {}
        for i in range(len(nums)):
            pfs += nums[i]
            # if pfs == k, it is one of the target subarray
            if pfs == k:
                res.append([0, i+1])
            # if pfs-k in hashtable, it is one of the target subarray
            remain = pfs - k
            if remain in ht:
                for start in ht[remain]:
                    res.append([start, i+1])
            # put the pfs into the hashtable
            if pfs not in ht:
                ht[pfs] = [i+1]
            else:
                ht[pfs].append(i+1)
        return res


print(Solution().subarraySum([1, 1, 1], 1))  # 3
print(Solution().subarraySum([1, 1, 1], 2))  # 2
print(Solution().subarraySum([1, 1, 1], 3))  # 1
print(Solution().subarraySum([1, 1, 1, 1], 3))  # 2
print(Solution().subarraySum([1, -1, 5, -2, 3], 3))  # 3
print(Solution().subarraySum([1, -1, 5, -2, 1, 2], 3))  # 4
print(Solution().subarraySum([-2, -1, 2, 1], 1))  # 2
print(Solution().subarraySum([-2, -1, 2, 1, 100], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 100, 1], 100))  # 2
print(Solution().subarraySum([-2, -1, 2, 1000], 99))  # 0
