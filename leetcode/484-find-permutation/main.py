"""
    1st approach: reverse subarray

    e.g.1
    D   D   I   I   D   I
    1   2   3   4   5   6   7
    _________       _____       <- reverse the order of items with continuous ^
    3   2   1   4   6   5   7   <- result

    Time    O(n)
    Space   O(n)
    76 ms, faster than 96.60%
"""


class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        N = len(s)
        res = []
        for i in range(1, N+2):
            res.append(i)
        i = 0
        while i < N:
            if s[i] != 'D':
                i += 1
                continue
            j = i
            while j < N and s[j] == 'D':
                j += 1
            self.reverse(res, i, j)
            i = j
        return res

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


print(Solution().findPermutation("IDIDDI"))
print(Solution().findPermutation("IIDDIIID"))
print("-----")

"""
    2nd approach: stack, suggested solution
    - basically when we see an 'D', we pile up the stack
    - when we see an 'I', we empty the stack and put the items into the result array
    
    ref:
    - https://leetcode.com/problems/find-permutation/solution/

    Time    O(n)
    Space   O(n)
    92 ms, faster than 64.63%
"""


class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        N = len(s)
        res = (N+1) * [0]
        stack = []
        j = 0
        for i in range(1, N+1):
            if s[i-1] == 'I':
                stack.append(i)
                while len(stack) > 0:
                    res[j] = stack.pop()
                    j += 1
            else:
                stack.append(i)
        stack.append(N+1)
        while len(stack) > 0:
            res[j] = stack.pop()
            j += 1
        return res


print(Solution().findPermutation("IDIDDI"))
print(Solution().findPermutation("IIDDIIID"))
