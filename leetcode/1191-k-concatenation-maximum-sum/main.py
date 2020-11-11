"""
    1st: kadan + pfs
    - basically the result would either
        - max subarray sum
        - prefixSum + (k-2) * sum(nums) + suffixSum
    - keep in mind that there might be some corner cases:
        - k < 2
        - sum(nums) < 0
    
    Time    O(N)
    Space   O(1)
    308 ms, faster than 72.60%
"""
class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        if k <= 0:
            return 0
        maxSubArraySum = self.kadane(arr)
        longSum = self.pfsMiddleSfs(arr, k)
        res = max(maxSubArraySum, longSum)
        if res < 0:
            return 0
        return res % (10**9 + 7)

    def kadane(self, nums):
        cur = -sys.maxsize
        res = -sys.maxsize
        for x in nums:
            cur = max(cur+x, x)
            res = max(res, cur)
        return res
    
    def pfsMiddleSfs(self, nums, k):
        if k == 1:
            return 0
        mpfs = 0
        pfs = 0
        for x in nums:
            pfs += x
            mpfs = max(mpfs, pfs)
        msfs = 0
        sfs = 0
        for i in range(len(nums)-1, -1, -1):
            x = nums[i]
            sfs += x
            msfs = max(msfs, sfs)
        middle = max(0, k - 2) * sum(nums)
        total = mpfs + max(middle, 0) + msfs
        return total