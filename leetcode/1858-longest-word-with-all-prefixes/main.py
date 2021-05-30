"""
    1st: hashtable
    - sort the words by length and alphabet
    - for each word, see if all of its prefixes can be found in hashtable
    - onyif found, put it in the hashtable

    P.S. it can be done with a trie, but it is a bit annoying to write

    Time    O(NlogN + NW)
    Space   O(N)
    340 ms, faster than 100.00%
"""


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda w: (len(w), w))
        seen = set()
        res = ''
        for w in words:
            word = ''
            shouldContinue = False
            for i in range(len(w)-1):
                word += w[i]
                if word not in seen:
                    shouldContinue = True
                    break
            if shouldContinue:
                continue
            if len(w) > len(res):
                res = w
            seen.add(w)
        return res
