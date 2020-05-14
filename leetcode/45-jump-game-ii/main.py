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

"""
    2nd: caching

    e.g.
    [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3]
     * 1 1 1 1 1 1 1 1
		       * 1 1 1 2 2 2 2 2 2
					   * 2 2 2 2 2 3 3 3
						     * 2 2 3 3 3 3

    Time    O(N^2)
    Space   O(N)
    LTE 80 / 92 test cases passed.
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        minSteps = len(nums) * [sys.maxsize]
        minSteps[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                k = i + j
                if k < len(nums):
                    minSteps[k] = min(minSteps[k], minSteps[i] + 1)
        return minSteps[-1]


"""
    3rd: binary search
    - optimize the above approach without saving count at every idx
    - just save the range and its count i.e. (idx, steps)
    e.g.
    [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3]
    
    What we gonna optimze is, we only store the minsteps at last the last index, therefore we can do binary search

    Orignal:
    [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3]
     * 1 1 1 1 1 1 1 1
		       * 1 1 1 2 2 2 2 2 2
					   * 2 2 2 2 2 3 3 3
						     * 2 2 3 3 3 3
    
    Optimal:
    [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3]
     * ------------> 1
		       * --------------> 2
					   * ------------> 3
						     * --------> 3 (2 + 1, becos the lower minsteps = 2, not 3)

    Time    O(NlogN)
    Space   O(N)
    148 ms, faster than 12.70%
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        minSteps = [(0, 0)]
        for i in range(len(nums)):
            k = min(i + nums[i], n - 1)
            if k > minSteps[-1][0]:
                idx = self.lowerBsearch(minSteps, i)
                if idx < len(minSteps):
                    minSteps.append((k, minSteps[idx][1] + 1))
                else:
                    minSteps.append((k, minSteps[-1][1] + 1))
        return minSteps[-1][1]

    def lowerBsearch(self, nums: List[tuple], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid][0]:
                right = mid
            else:
                left = mid + 1
        return left


"""
    4th: dynamic programming? greedy?
    - similar to lc55: Jump Game I
    - here we have 2 more variables
        - jumps: track the number of jumps
        - gMaxIdx: track the global farthest index we can reach
    
    Time    O(N)
    Space   O(1)
    96 ms, faster than 77.02%
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        maxIdx = 0
        gMaxIdx = 0
        jumps = 0
        for i in range(len(nums)):
            if i > gMaxIdx:
                jumps += 1
                gMaxIdx = maxIdx
            maxIdx = max(maxIdx, i+nums[i])
        return jumps
