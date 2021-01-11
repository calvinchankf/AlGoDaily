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

    Time    O(NNW)     NW = iterating W words and slice a string of N length, N = do it N times because there are N remaining strings
    Space   O(N+N)      N= remaining strings, N= recursion tree depth
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

print("-----")


"""
    2nd: use index instead of slicing
    - so the length of every key is smaller in the hashtable
    - but if the string is long and wordDict is small, it will be slow

    Time    O(N^3)
    Space   O(N+N)
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        return self.dfs(s, 0, wordSet, {})

    def dfs(self, s, start, wordSet, ht):
        if start == len(s):
            return True

        if start in ht:                 # O(N): N times
            return False

        for i in range(start, len(s)):  # O(N^2): do slicing at every index
            sub = s[start: i+1]
            if sub in wordSet and self.dfs(s, i+1, wordSet, ht):
                return True
        ht[start] = False
        return False


"""
    3rd: BFS

    Time    O(N^3)
    Space   O(N)
    36 ms, faster than 79.99%
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        cache = {}
        q = [0]
        while len(q) > 0:
            start = q.pop(0)
            if start == len(s):
                return True
            if start in cache:
                continue
            cache[start] = False
            for i in range(start, len(s)):
                sub = s[start: i+1]
                if sub in wordSet:
                    q.append(i+1)
        return False
