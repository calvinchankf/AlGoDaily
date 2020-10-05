"""
    questions to ask:
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
            prefix = s[:n]
            if prefix == w:
                options = self.dfs(s[n:], wordSet, ht)
                for sf in options:
                    sentence = w + ' ' + sf
                    sentences.append(sentence.strip())
        ht[s] = sentences
        return ht[s]


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
