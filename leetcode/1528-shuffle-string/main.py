"""
    Time    O(2N)
    Space   O(N)
    36 ms, faster than 91.44%
"""
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n = len(s)
        chars = n * ['']
        for i in range(n):
            newIdx = indices[i]
            chars[newIdx] = s[i]
        return ''.join(chars)