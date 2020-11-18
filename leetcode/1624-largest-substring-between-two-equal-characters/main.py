"""
    1st: kind of brute force
    - use a hashtable to store seen explored characters
    - find the target from the back to form the longest substring in between

    Time    O(26N)
    Space   O(26)
    16 ms, faster than 92.07%
"""
class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = -1
        seen = set()
        for i in range(len(s)):
            target = s[i]
            if target in seen:
                continue
            seen.add(target)
            for j in range(len(s)-1, i, -1):
                if s[j] == target:
                    res = max(res, j - i - 1)
                    break
        return res