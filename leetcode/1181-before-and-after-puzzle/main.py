"""
    1st: better brute force with hashtables

    Time    O(N + N^2 + NNlogNN)
    Time    O(N)
    48 ms, faster than 34.15%
"""


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        n = len(phrases)

        firsts = {}
        lasts = {}

        for i in range(n):
            s = phrases[i]
            words = s.split()
            first = words[0]
            last = words[-1]
            firsts[i] = [first, ' '.join(words[1:])]  # [first, remain]
            lasts[i] = last

        res = set()
        for i in range(n):
            lastWord = lasts[i]
            for j in range(n):
                if i == j:
                    continue
                firstWord, remain = firsts[j]
                if lastWord == firstWord:
                    temp = phrases[i] + ' ' + remain
                    res.add(temp.strip())
        return sorted(list(res))
