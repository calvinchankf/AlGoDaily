"""
    1st: hashtable
    - use hashtable to store the occurence of every character when we go forward
    - get the hashtable from the back(ward) by subtracting forward[i] from total
    - compare the hashtables

    Time    O(N)
    Space   O(N)
    1852 ms, faster than 25.00%
"""


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)

        total = 26 * [0]
        for i in range(n):
            c = s[i]
            key = ord(c) - ord('a')
            total[key] += 1

        res = 0
        forward = 26 * [0]
        for i in range(n):
            c = s[i]
            key = ord(c) - ord('a')
            forward[key] += 1
            f, b = 0, 0
            for i in range(26):
                if forward[i] > 0:
                    f += 1
                if total[i] - forward[i] > 0:
                    b += 1
            if f == b:
                res += 1
        return res
