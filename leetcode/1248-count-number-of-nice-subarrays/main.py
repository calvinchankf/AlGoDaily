"""
    1st: sliding window(2 pointers)
    - similar to lc3, 159, 340, 992

    - the crux of the problem based on the fact that:
        1. atMostK(nums, K) - atMostK(nums, K-1) = exactlyK(nums, K)
        2. to find the number of subarrays with atMost K, we use res += i - j + 1

    e.g.

    aabab
    1       <- a
     2      <- a, aa
      3     <- b, ab, aab
       4    <- a, ba, aba, aaba
        5   <- b, ab, bab, abab, aabab
    so there total 16 substrings that at most have 2 distinct charactors

    Time    O(N)
    Space   O(1)
    1008 ms, faster than 46.80%
"""


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k-1)

    def atMostK(self, nums, k):
        oddCount = 0
        j = 0
        res = 0
        for i in range(len(nums)):
            oddCount += nums[i] % 2
            while oddCount > k:
                last = nums[j]
                j += 1
                oddCount -= last % 2
            res += i - j + 1
        return res
