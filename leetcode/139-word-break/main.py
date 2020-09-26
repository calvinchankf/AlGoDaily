"""
    1st approach: recursion + memorization
    - e.g. "catsandogab", ["cats", "dog", "sand", "and", "cat", "og", "ab"]
        from the begining, we can split it into 2 strings
        [cat,sandogab], [cats, andogab]
        then they can become in the next recursion
        [cat,sand,ogab], [cat,sand,ogab]
        then 
        [cat,sand,og,ab], [cat,sand,og,ab]
    - actually we did [cat,sand,ogab], we know that "ogab" is breakable after the recursion,
        therefore we can save "ogab" as "true" so that we can avoid redundant computation if we meet "ogab" again

    Time    O(n^2) whereas brute force O(N^N)
    Space   O(n)

    32 ms, faster than 57.40%
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set()
        for w in wordDict:
            wordSet.add(w)
        m = {}
        return self.find(s, wordSet, m)

    def find(self, s, wordSet, m):
        if len(s) == 0:
            return True
        if s in m:
            return m[s]
        ifAnyTrue = False
        for i in range(1, len(s)+1):
            w = s[:i]
            if w in wordSet:
                temp = self.find(s[i:], wordSet, m)
                ifAnyTrue = ifAnyTrue or temp
        m[s] = ifAnyTrue
        return ifAnyTrue


s = "applepenapple"
d = ["apple", "pen"]
print(Solution().wordBreak(s, d))

s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))

s = "catsanddog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))

s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat", "og"]
print(Solution().wordBreak(s, d))

a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
d = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
     "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(Solution().wordBreak(s, d))

print("----------------------------------------")

"""
    2nd approach: recursion + memorization + slice max length
    - e.g. "catsandogab", ["cats", "dog", "sand", "and", "cat", "og", "ab"]
    from the begining, we can split it into 2 strings
    [cat,sandogab], [cats, andogab]
    then they can become in the next recursion
    [cat,sand,ogab], [cat,sand,ogab]
    then 
    [cat,sand,og,ab], [cat,sand,og,ab]
    - actually we did [cat,sand,ogab], we know that "ogab" is breakable after the recursion,
    therefore we can save "ogab" as "true" so that we can avoid redundant computation if we meet "ogab" again

    Time    O(n^2)
    Space   O(n)
    16 ms, faster than 99.95%
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, {})

    def dfs(self, s, wordSet, ht):
        if len(s) == 0:
            return True
        if s in ht:
            return False
        for w in wordSet:
            n = len(w)
            prefix = s[:n]
            if prefix == w:
                if self.dfs(s[n:], wordSet, ht):
                    return True
        ht[s] = False
        return ht[s]


s = "applepenapple"
d = ["apple", "pen"]
print(Solution().wordBreak(s, d))

s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))

s = "catsanddog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))

s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat", "og"]
print(Solution().wordBreak(s, d))

a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
d = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
     "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(Solution().wordBreak(s, d))
