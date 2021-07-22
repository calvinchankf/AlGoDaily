"""
    1st: brute force backtracking
    
    Time    O(N * 2^N)
    Space   O(2^N)
    LTE
"""


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        digits = self.num2Bin(n, start)
        self.seq = []
        startKey = tuple(digits)
        self.backtrack(n, digits, set([startKey]), [startKey])
        res = []
        for key in self.seq:
            res.append(self.bin2Num(key))
        return res

    def backtrack(self, n, digits, used, seq):
        if len(used) == 2**n:
            self.seq = seq
            return True
        for i in range(len(digits)):
            _digits = digits[:]
            _digits[i] ^= 1
            key = tuple(_digits)
            if key in used:
                continue
            used.add(key)
            if self.backtrack(n, _digits, used, seq + [key]):
                return True
            used.remove(key)
        return False

    def num2Bin(self, n, x):
        digits = n * [0]
        i = 0
        while x > 0:
            digits[i] = x & 1
            x >>= 1
            i += 1
        return digits[::-1]

    def bin2Num(self, digits):
        res = 0
        j = 0
        for i in range(len(digits)-1, -1, -1):
            res += (2**j) * digits[i]
            j += 1
        return res


"""
    2nd: bit op
    - this is based on the classic problem lc89: gray code
    - when it starts at 0, there will be a destined sequence
    - and we can just rotate the sequence with the first item == start

    Time    O(2^N)
    Space   O(2^N)
    240 ms, faster than 28.57%
"""


class Solution(object):
    def circularPermutation(self, n, start):
        grayCodes = []
        for i in range(2**n):
            grayCodes.append(i ^ (i >> 1))
        i = grayCodes.index(start)
        return grayCodes[i:] + grayCodes[:i]


"""
    3rd: elegant approach by the others
    - same as 2nd approach

    388 ms, faster than 20.34%
"""


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ i >> 1 for i in range(1 << n)]
