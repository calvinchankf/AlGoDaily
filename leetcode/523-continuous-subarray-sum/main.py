"""
    2nd: zero sum subarray
    - similar to lc325, 525, 560, 930, 1124, 1171
    - rephase: finding a subarray that sum to 0(mod-ed prefix sum)

    e.g.1 [23, 2, 4, 6, 7], 6
    pfs   5   1  5
          ^      ^
    the mod-ed pfs comes back to 5, it means there is a subarray [2,4] can sum up to 6

    e.g.2 [23, 8, 10, 6, 7], 6
    pfs   5   1   5
          ^       ^
    the mod-ed pfs comes back to 5, it means there is a subarray [2,4] can sum up to 6

    Time    O(N)
    Space   O(N)
    84 ms, faster than 76.47% 
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ht = {}
        pfs = 0
        for i in range(n):
            pfs += nums[i]
            if k != 0:
                pfs = pfs%k
            if pfs == 0 and i > 0:
                return True
            if pfs in ht and ht[pfs] + 1 < i:
                return True
            if pfs not in ht:
                ht[pfs] = i
        return False