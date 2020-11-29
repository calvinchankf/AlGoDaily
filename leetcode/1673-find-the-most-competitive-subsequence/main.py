"""
    1st: stack
    - keep the current number to the bottom of the stack as much as possible

    e.g.1
    [3,5,2,6] k=2
    at idx1, stack = [3, 5]
    at idx2, cur = 2, we know we can pop the whole stack becos we still have 2 items remaining in the array. So stack = [2]
    at idx3, stack = [2, 6]

    Time    O(N)
    Space   O(N)
    1448ms
"""


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []
        for i in range(n):
            x = nums[i]
            while len(stack) > 0 and x < stack[-1] and n - i + len(stack) - 1 >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(x)
        return stack
