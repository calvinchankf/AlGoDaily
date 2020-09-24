import sys
from collections import defaultdict
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

print("-----")

"""
    2nd: lc560 + lc646
    LTE 65 / 69 test cases passed.
"""


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        intvs = []
        pfs = 0
        ht = defaultdict(list)
        for i in range(len(nums)):
            pfs += nums[i]
            if pfs == target:
                intvs.append((0, i))
            remain = pfs - target
            if remain in ht:
                for idx in ht[remain]:
                    intvs.append((idx+1, i))
            ht[pfs].append(i)

        intvs = sorted(intvs, key=lambda x: x[1])
        count = 0
        pos = -sys.maxsize
        for s, e in intvs:
            if s > pos:
                pos = e
                count += 1
        return count
