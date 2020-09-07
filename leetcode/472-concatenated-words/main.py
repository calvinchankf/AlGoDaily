"""
    questions to ask:
    - duplicate words? maybe
    - lower case == upper case? no
    - if a word cannot be splited, is it a compound word? no, it is not so dont put it into the result
"""

"""
    1st approach: recursion + hashtable (dynamic programming)

    Time    < O(n*2^k) k: average number of characters of words, but since we use hashtable, it must be smaller
    Space   < O(2^k) the recursion tree, but since we use hashtable, it must be smaller
    1260 ms, faster than 38.58%
    14may2019
"""


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # put words in set for faster lookup
        wordSet = set(words)
        seen = {}
        res = []
        # for each word, count the number of slices we can cut
        for word in wordSet:
            count = self.dfs(word, wordSet, seen)
            if count > 1:
                res.append(word)
        return res

    def dfs(self, s, wordSet, seen):
        if len(s) == 0:
            return 1
        # avoid redundant calculation
        if s in seen:
            return seen[s]
        count = 0
        # slice characters instead of iterating the wordSet
        # because there might be so many words here for this question
        for i in range(len(s)):
            temp = s[:i+1]
            # slice if see any
            if temp in wordSet:
                count += self.dfs(s[i+1:], wordSet, seen)
        seen[s] = count
        return count


a = ["cat", "catdog", "dog"]
print(Solution().findAllConcatenatedWordsInADict(a))

a = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
     "hippopotamuses", "rat", "ratcatdogcat"]
print(Solution().findAllConcatenatedWordsInADict(a))

a = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog",
     "hippopotamuses", "rat", "ratcatdogcat", "hippo", "potamuses"]
print(Solution().findAllConcatenatedWordsInADict(a))
