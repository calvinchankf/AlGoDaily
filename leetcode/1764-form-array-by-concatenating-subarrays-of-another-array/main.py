"""
    1st: 2 pointers
    - this is amazon OA: fresh promotion

    Time    O(N)
    Space   O(1)
    108 ms, faster than 50.00% 
"""


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0  # groups
        j = 0  # nums
        while i < len(groups) and j + len(groups[i]) <= len(nums):
            matchCount = 0
            codes = groups[i]
            for k in range(len(codes)):
                if codes[k] == nums[j+k]:
                    matchCount += 1
                else:
                    break
            # if the groups[i] matches part of the nums
            if matchCount == len(codes):
                i += 1
                j += len(codes)
            else:
                j += 1
        return i == len(groups)
