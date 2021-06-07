"""
    1st: brute force comparison
    - actually there are only 2 possibilities:
        - 01010101....
        - 10101010....
    - just compare the swapCounts to make the input string to both of the possibilities

    Time    O(N)
    Space   O(N)
    48 ms, faster than 29.40%
"""


class Solution:
    def minSwaps(self, s: str) -> int:
        nums = [int(c) for c in s]
        n = len(s)
        zeroFirst = n * [0]
        oneFirst = n * [0]
        for i in range(n):
            if i % 2 == 0:
                zeroFirst[i] = 1
            else:
                oneFirst[i] = 1

        a = self.countSwap(nums, zeroFirst)
        b = self.countSwap(nums, oneFirst)
        res = min(a, b)

        if res == 2**32:
            return -1
        return res

    def countSwap(self, nums, target):
        n = len(nums)
        zero2oneCount = 0
        one2zeroCount = 0
        for i in range(n):
            if nums[i] == 0 and target[i] == 1:
                zero2oneCount += 1
            if nums[i] == 1 and target[i] == 0:
                one2zeroCount += 1
        if zero2oneCount == one2zeroCount:
            return one2zeroCount
        return 2**32
