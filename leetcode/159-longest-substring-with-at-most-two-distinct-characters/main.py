from collections import Counter


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        j = 0
        ht = Counter()
        res = 0
        for i in range(len(s)):
            cur = s[i]
            ht[cur] += 1
            while len(ht) > 2:
                left = s[j]
                j += 1
                ht[left] -= 1
                if ht[left] == 0:
                    del ht[left]
            res = max(res, i-j+1)
        return res
