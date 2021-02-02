"""
    3rd approach: sliding window
    - similar to lc438

    Time    O(A+B)
    Space   O(52)
    100 ms, faster than 21.89%
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        target = 26 * [0]
        for c in s1:
            idx = ord(c) - ord('a')
            target[idx] += 1
        res = []
        j = 0
        window = 26 * [0]
        for i in range(len(s2)):
            c = s2[i]
            idx = ord(c) - ord('a')
            window[idx] += 1
            if i >= len(s1):
                left = s2[j]
                idx = ord(left) - ord('a')
                window[idx] -= 1
                j += 1
            if self.isMatched(target, window):
                return True
        return False

    def isMatched(self, a, b):
        for i in range(26):
            if a[i] != b[i]:
                return False
        return True
