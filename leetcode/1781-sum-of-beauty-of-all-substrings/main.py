"""
    1st: better brute force with hashtable

    Time    O(26 N^2)
    Time    O(1)
    11084 ms, faster than 100.00%
"""
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            counts = 26 * [0]
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                counts[idx] += 1
                minFreq = n
                maxFreq = 0
                for f in counts:
                    if f > 0:
                        minFreq = min(minFreq, f)
                        maxFreq = max(maxFreq, f)
                res += max(maxFreq - minFreq, 0)
        return res