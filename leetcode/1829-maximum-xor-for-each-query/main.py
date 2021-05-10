"""
    1st: bit op
    - cache all the XORs result for every index
    - for every number, the way to maximize K is
        e.g. XORS[i] = 101, maxBit = 4

            0101 <- xors[i]
            1111 <- maxBit
        --------
            1010 <- the best value K

    Time    O(N + NB)
    Space   O(N)
    3484 ms, faster than 100.00%
"""


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xors = n * [0]
        xors[0] = nums[0]
        for i in range(1, n):
            xors[i] = xors[i-1] ^ nums[i]
        res = n * [0]
        for i in range(n):
            x = xors[n-i-1]
            k = 0
            for j in range(maximumBit):
                if x & 1 == 0:
                    k += 2**j
                x >>= 1
            res[i] = k
        return res
