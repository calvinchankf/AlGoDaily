"""
    1st: greedy?
    - there are only 2 possibilites, 010101... OR 101010...
    - count the diff of S between the above two

    Time    O(N)
    Space   O(1)
    48 ms, faster than 100.00%
"""


class Solution:
    def minOperations(self, s: str) -> int:
        zeroOne = 0
        oneZero = 0
        for i in range(len(s)):
            c = s[i]
            if i % 2 == 0:
                if c != '0':
                    zeroOne += 1
                else:
                    oneZero += 1
            else:
                if c != '1':
                    zeroOne += 1
                else:
                    oneZero += 1
        return min(zeroOne, oneZero)
