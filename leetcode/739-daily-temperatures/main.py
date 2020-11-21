"""
    1st approach: stack
    
    Time    O(2n)
    Space   O(n)
    460 ms, faster than 53.26%
"""


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        n = len(T)
        res = n * [0]
        stack = []  # item, index
        for i in range(n):
            while len(stack) > 0 and stack[-1][0] < T[i]:
                _, j = stack.pop()
                res[j] = i - j
            stack.append((T[i], i))
        return res
