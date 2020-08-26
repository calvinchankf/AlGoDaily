"""
    1st approach: subarray sum = k
    - this question is fucking similar to leetcode 325, 523, 525, 560, 1124, 1171
    
    generic approach
    - find loops <==============================================================
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: number of occurence of a previous sum
        - if currentSum - target in the hastable, the result+1

    Time	O(n)
    Space   O(n)
    228 ms, faster than 53.26%
"""


class Solution(object):
    def numSubarraysWithSum(self, nums, k):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        res = 0
        prevsum = 0
        # key: previous sum, value: number of occurence of a previous sum
        m = {}
        for num in nums:
            prevsum += num
            # if prevsum == k, it is one of the target subarray
            if prevsum == k:
                res += 1
            # if prevsum-k in hashtable, it is one of the target subarray
            if prevsum-k in m:
                res += m[prevsum-k]
            # put the prevsum into the hashtable
            if prevsum not in m:
                m[prevsum] = 1
            else:
                m[prevsum] += 1
        return res
