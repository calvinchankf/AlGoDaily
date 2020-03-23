class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        merge = x ^ y
        count = 0
        while merge > 0:
            if merge & 1 == 1:
                count += 1
            merge = merge >> 1
        return count


print(Solution().hammingDistance(1, 4))

"""
    2nd: bit op
    - get the bit operation of both numbers
    - find the diff

    Time    O(logM + logN)
    Space   O(64)
    44 ms, faster than 5.17%
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = self.binary(x)
        by = self.binary(y)
        res = 0
        for i in range(32):
            res += abs(bx[i] - by[i])
        return res

    def binary(self, n):
        b = 32 * [0]
        idx = 0
        while n > 0:
            b[idx] = n % 2
            n >>= 1
            idx += 1
        return b
