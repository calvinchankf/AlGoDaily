"""
    questions to ask:
    - similar to lc131, 132, 139, 140
    - will the words in wordDict contain each other? e.g. wordDict = [abc, ab] ? yes
    - will there be no duplicate words in wordDict? yes
    - lowercase letters only? yes
    - do we need to deal with punctuation? no
"""

"""
    classic approach: bottom-up recursion + memorization
    - similar to lc132
    - see ./idea.png

    ref:
    - https://leetcode.com/problems/word-break-ii/discuss/44167/My-concise-JAVA-solution-based-on-memorized-DFS

    Time    O(N^2 + 2^N + W) Size of recursion tree can go up to n^2. The creation of list takes k time.
    Space   O(2^N + W)
    44 ms, faster than 47.57%
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, {})

    def dfs(self, s, wordSet, ht):
        if len(s) == 0:
            return ['']
        if s in ht:
            return ht[s]
        sentences = []
        for w in wordSet:
            n = len(w)
            sub = s[:n]
            if w == sub:
                cands = self.dfs(s[n:], wordSet, ht)
                for cand in cands:
                    sentence = w + ' ' + cand
                    sentences.append(sentence.strip())
        ht[s] = sentences
        return sentences


s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))
print("---")

s = "catsanddog"
d = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, d))
print("---")

s = "pineapplepenapple"
d = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, d))
print("---")

s = "pineapplepenapple"
d = ["apple", "pen", "applepen", "pine", "pineapple", "penapple"]
print(Solution().wordBreak(s, d))
print("---")

s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))
print("---")

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
d = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
     "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(Solution().wordBreak(s, d))

print("-----")

"""
    2nd: use index instead of slicing
    - so the length of every key is smaller in the hashtable
    - but if the string is long and wordDict is small, it will be slow
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        return self.dfs(s, 0, wordSet, {})

    def dfs(self, s, start, wordSet, ht):
        if start == len(s):
            return ['']

        if start in ht:                 # O(N): N times
            return ht[start]

        sentences = []
        for i in range(start, len(s)):  # O(N^2): do slicing at every index
            sub = s[start: i+1]
            if sub in wordSet:
                suffixes = self.dfs(s, i+1, wordSet, ht)
                for sf in suffixes:
                    temp = sub + ' ' + sf
                    sentences.append(temp.strip())

        ht[start] = sentences
        return sentences
