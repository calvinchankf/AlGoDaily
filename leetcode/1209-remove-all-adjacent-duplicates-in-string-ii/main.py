"""
    stack

    Time    O(N)
    Space   O(N)
    80 ms, faster than 46.97%
"""


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for c in s:
            if len(stack) > 0 and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if len(stack) > 0 and stack[-1][1] == k:
                stack.pop()
        res = ''
        for char, count in stack:
            res += char * count
        return res


s = Solution()

a = "abcd"
b = 2
print(s.removeDuplicates(a, b))

a = "aabbccdd"
b = 2
print(s.removeDuplicates(a, b))

a = "deeedbbcccbdaa"
b = 3
print(s.removeDuplicates(a, b))

a = "pbbcggttciiippooaais"
b = 2
print(s.removeDuplicates(a, b))
