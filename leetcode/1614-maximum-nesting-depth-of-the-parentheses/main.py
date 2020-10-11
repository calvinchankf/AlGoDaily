class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        openCount = 0
        res = 0
        for c in s:
            if c == '(':
                openCount += 1
            elif c == ')':
                if openCount > 0:
                    openCount -= 1
            else:
                res = max(res, openCount)
        return res