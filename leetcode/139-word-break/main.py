"""
    1st approach: recursion + memorization + slice max length
    - similar to lc131, 132, 139, 140
    
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
    12 ms, faster than 99.83%
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, {})

    def dfs(self, s, wordSet, ht):
        if len(s) == 0:
            return True
        if s in ht:  # or use len(s) as the key
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
