"""
    1st: recursion
    - based on the classic subset problem lc78, try all the possibilities

    Time    O(2^N) N = words count
    Space   O(2^N) the recursion tree
    60 ms, faster than 62.84%
"""


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        letterCounts = 26 * [0]
        for c in letters:
            i = ord(c) - ord('a')
            letterCounts[i] += 1

        letterScores = score[:]  # 26 * [0]

        self.res = 0
        self.dfs(words, letterCounts, letterScores, 0)
        return self.res

    def dfs(self, words, letterCounts, letterScores, curScore):

        self.res = max(self.res, curScore)

        for i in range(len(words)):
            w = words[i]

            needs = 26 * [0]
            for c in w:
                j = ord(c) - ord('a')
                needs[j] += 1

            canFulfill = True
            for j in range(26):
                if needs[j] > letterCounts[j]:
                    canFulfill = False
                    break

            if not canFulfill:
                continue

            _letterCounts = letterCounts[:]
            scoreToAdd = 0
            for j in range(26):
                scoreToAdd += letterScores[j] * needs[j]
                _letterCounts[j] -= needs[j]

            self.dfs(
                words[i+1:],
                _letterCounts,
                letterScores,
                curScore + scoreToAdd
            )
