import sys
"""
    0th: brute force recursion

    Time    O(n * 2^n) the worst case all characters are the same, so for each character we can split or contain
    Space   O(n) the depth of the recursion tree
    LTE
"""


class Solution(object):

    def minCut(self, s):
        self.res = []
        self.dfs(s, [])
        return min([len(x) for x in self.res]) - 1

    def dfs(self, s, cur):
        if len(s) == 0:
            self.res.append(cur)
            return
        for i in range(len(s)):
            sub = s[:i+1]
            if sub == sub[::-1]:
                self.dfs(s[i+1:], cur + [sub])


s = Solution()

a = 'aab'
print(s.minCut(a))

a = 'a'
print(s.minCut(a))

a = 'ab'
print(s.minCut(a))

a = 'noonabbad'
print(s.minCut(a))

print("-----")

"""
    1st: dynamic programming (recursion + hashtable)
    - similar to lc131, 132, 139, 140
    - cache only stores the minLength group of palindrome from the end of the string

    e.g. 'noonabbad'
    'd': ['d']
    'ad': ['d', 'a']
    'bad': ['d', 'a', 'b']
    'bbad': ['d', 'a', 'bb']
    'abbad': ['d', 'abba']
    'nabbad': ['d', 'abba', 'n']
    'onabbad': ['d', 'abba', 'n', 'o']
    'oonabbad': ['d', 'abba', 'n', 'oo']
    'noonabbad': ['d', 'abba', 'noon']
    
    The result cache is 'noonabbad': ['d', 'abba', 'noon']
    Hence, the result is 3 - 1 = 2

    Time    O(N^2) in each recursion we check every suffix O(N), and there are N recursions (because every recursion stops when we see a cache)
    Space   O(N) the suffixes cache
    2076 ms, faster than 5.29%
"""


class Solution(object):

    def minCut(self, s):
        res = self.dfs(s, {})
        return len(res) - 1

    def dfs(self, s, ht):
        if len(s) == 0:
            return []
        if s in ht:
            return ht[s]
        minGroup = None
        forward = ''
        backward = ''
        for i in range(len(s)):
            forward += s[i]
            backward = s[i] + backward
            if forward == backward:
                group = self.dfs(s[i+1:], ht) + [forward]
                if minGroup == None or len(group) < len(minGroup):
                    minGroup = group
        print(s, minGroup)
        ht[s] = minGroup
        return ht[s]


s = Solution()

a = 'aab'
print(s.minCut(a))

a = 'a'
print(s.minCut(a))

a = 'ab'
print(s.minCut(a))

a = 'noonabbad'
print(s.minCut(a))

a = "ababababababababababababcbabababababababababababa"
print(s.minCut(a))

a = "cabababcbc"
print(s.minCut(a))

a = "bobnoonabbadnxna"
print(s.minCut(a))

print("-----")


"""
    2nd: dynamic programming (recursion + hashtable)
    - similar to lc139,140
    - cache only stores the minLength group of palindrome from the end of the string

    e.g. 'noonabbad'
    'd': 1
    'ad': 2
    'bad': 3
    'bbad': 3
    'abbad': 2
    'nabbad': 3
    'onabbad': 4
    'oonabbad': 4
    'noonabbad': 3
    
    The result cache is 'noonabbad': ['', 'd', 'abba', 'noon'], then we ignore the empty string.
    Hence, the result is 3 - 1 = 2

    Time    O(N^2) in each recursion we check every suffix O(N), and there are N recursions (because every recursion stops when we see a cache)
    Space   O(N) the suffixes cache
    884 ms, faster than 13.70%
"""


class Solution(object):

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = self.dfs(s, {})
        return res - 1

    def dfs(self, s, ht):
        if len(s) == 0:
            return 0
        if s in ht:
            return ht[s]
        minGroupLen = sys.maxsize
        for i in range(len(s)):
            sub = s[:i+1]
            if sub == sub[::-1]:
                groupLen = self.dfs(s[i+1:], ht) + 1
                if groupLen < minGroupLen:
                    minGroupLen = groupLen
        # print(s, minGroup)
        ht[s] = minGroupLen
        return ht[s]


s = Solution()

a = 'aab'
print(s.minCut(a))

a = 'a'
print(s.minCut(a))

a = 'ab'
print(s.minCut(a))

a = 'noonabbad'
print(s.minCut(a))

a = "ababababababababababababcbabababababababababababa"
print(s.minCut(a))

a = "cabababcbc"
print(s.minCut(a))

a = "bobnoonabbadnxna"
print(s.minCut(a))
