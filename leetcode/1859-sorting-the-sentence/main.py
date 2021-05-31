"""
    1st: string slicing + sorting
    - for every word, extract the digits from the end => ranking
    - sort the words by their ranking

    Time    O(NlogN)
    Space   O(N)
    32 ms, faster than 50.00%
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        mapping = []
        for w in words:
            word, ranking = self.separateWord(w)
            mapping.append((word, ranking))
        mapping.sort(key=lambda x: x[1])
        arr = [x[0] for x in mapping]
        return ' '.join(arr)

    def separateWord(self, w):
        ranking = 0
        N = len(w)
        i = N - 1
        while i >= 0 and w[i].isdigit():
            d = int(w[i])
            ranking += d * (10**(N - i - 1))
            i -= 1
        return w[:i+1], ranking
