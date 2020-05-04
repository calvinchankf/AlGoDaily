"""
    1st: bit op
    - same as lc1009
    - if the current bit is 0, add 1 << count the result
    - increment the count and N//2 when we iterating through the binary representation of the number

    Time    O(logn)
    Space   O(1)
    32 ms, faster than 37.10%
"""


class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        res = 0
        i = 0
        while num > 0:
            temp = num & 1
            res += abs(temp - 1) * (2**i)
            num >>= 1
            i += 1
        return res
