import sys

"""
    1st: bfs + hashtable
    LTE 80 / 92 test cases passed.
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        minSteps = len(nums) * [sys.maxsize]
        q = [(0, 0)]
        while len(q) > 0:
            idx, steps = q.pop(0)
            num = nums[idx]
            if idx + 1 >= len(nums):
                return steps
            if steps >= minSteps[idx] or num == 0:
                continue
            for i in range(1, num + 1):
                q.append((idx + i, steps + 1))
        return -1
