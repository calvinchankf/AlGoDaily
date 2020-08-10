from typing import List

"""
    1st: hashtable
    - similar to lc325, 525, 560, 930, 1124, 1171
    - whenever we see a subarray sum=target
        1. res += 1
        2. reset prefix sum = 0
        3. clean up hashtable
    - it means e.g. nums = [-1,3,5,1,4,2,-9], target = 6

    `<` from
    `>` to
    nums = [-1, 3, 5, 1, 4, 2, -9]
                   <  > clean up hashtable
                         <  > clean up hashtable
            <                   > even sum(nums[1:7]) == target, since at -9, the prefix sum from -1 has been cleaned-up

    Time    O(N)
    Space   O(N)
    648 ms, faster than 60.00%
"""


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        res = 0
        pfs = 0
        seen = {0}
        for i in range(len(nums)):
            pfs += nums[i]
            if pfs - target in seen:
                res += 1
                pfs = 0
                seen = {0}
            else:
                seen.add(pfs)
        return res


s = Solution()

print(s.maxNonOverlapping([1, 1, 1, 1, 1], 2))  # 2
print(s.maxNonOverlapping([-1, 3, 5, 1, 4, 2, -9], 6))  # 2
print(s.maxNonOverlapping([-2, 6, 6, 3, 5, 4, 1, 2, 8], 10))  # 3
