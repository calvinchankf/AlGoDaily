"""
    1st: sliding window

    Time    O(N)
    Space   O(K)
    1320 ms, faster than 100.00%
"""


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        ht = {}
        ans = []
        j = 0
        for i in range(len(nums)):

            if nums[i] not in ht:
                ht[nums[i]] = 0
            ht[nums[i]] += 1

            if i >= k:
                ht[nums[j]] -= 1
                if ht[nums[j]] == 0:
                    del ht[nums[j]]
                j += 1

            if i >= k-1:
                ans.append(len(ht))
        return ans
