"""
    1st approach: sliding window + hashtable
    - similar to lc195,395

    Time    O(26S)
    Space   O(26)
    104 ms, faster than 13.70%
"""


from collections import *


class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        res = 0
        counts = 26 * [0]
        for i in range(len(S)):
            if i >= K:
                last = S[i-K]
                idx = ord(last) - ord('a')
                counts[idx] -= 1
            c = S[i]
            idx = ord(c) - ord('a')
            counts[idx] += 1
            if self.ifAllOnes(counts, K):
                res += 1
        return res

    def ifAllOnes(self, counts, K):
        cnt = 0
        for i in range(len(counts)):
            if counts[i] > 1:
                return False
            cnt += counts[i]
        return cnt == K


"""
    2nd approach: sliding window + hashtable
    - similar to lc195,395

    Time    O(26S)
    Space   O(26)
    64 ms, faster than 28.61%
"""


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        ht = Counter()
        res = 0
        for i in range(len(S)):
            c = S[i]
            ht[c] += 1
            if i >= K:
                left = S[i-K]
                ht[left] -= 1
                if ht[left] == 0:
                    del ht[left]
            if len(ht) == K:
                res += 1
        return res
