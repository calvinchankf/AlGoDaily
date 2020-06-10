from typing import List

"""
    1st: min-max shit
    - in fact, there are 2 cases
        1. numbers at even index is greater
        2. numbers at odd index is greater
    - lets mutate an array to fit case 1
        - basically, we only care about the number at odd index, we want nums[i] = min(nums[i-1], nums[i+1])
    - lets do the same for case 2 with the same technique
        - but on even-indexed numnber

    Time    O(N)
    Space   O(N)
    40 ms, faster than 19.05% 
"""


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        evenGreater = nums[:]
        oddGreater = nums[:]

        resEven = 0
        for i in range(len(nums)):
            left = evenGreater[i-1] if i-1 >= 0 else evenGreater[i+1]
            right = evenGreater[i+1] if i+1 < len(nums) else left
            if i % 2 == 1:
                if evenGreater[i] >= left or evenGreater[i] >= right:
                    temp = evenGreater[i]
                    evenGreater[i] = min(left, right) - 1
                    resEven += temp - evenGreater[i]

        resOdd = 0
        for i in range(len(nums)):
            left = oddGreater[i-1] if i-1 >= 0 else oddGreater[i+1]
            right = oddGreater[i+1] if i+1 < len(nums) else left
            if i % 2 == 0:
                if oddGreater[i] >= left or oddGreater[i] >= right:
                    temp = oddGreater[i]
                    oddGreater[i] = min(left, right) - 1
                    resOdd += temp - oddGreater[i]

        return min(resEven, resOdd)
