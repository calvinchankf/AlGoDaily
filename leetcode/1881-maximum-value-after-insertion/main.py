"""
    1st: greedy
    - for a positive number, insert X in front of the first smaller digit
    - for a negative number, insert X in front of the first bigger digit

    Time    O(N)
    Space   O(1)
    104 ms, faster than 80.00%
"""


class Solution:
    def maxValue(self, n: str, x: int) -> str:

        N = len(n)

        if n[0] == '-':
            j = N
            for i in range(1, N):
                if x < int(n[i]):
                    j = i
                    break
            return n[:j] + str(x) + n[j:]

        j = N
        for i in range(N):
            if x > int(n[i]):
                j = i
                break

        return n[:j] + str(x) + n[j:]
