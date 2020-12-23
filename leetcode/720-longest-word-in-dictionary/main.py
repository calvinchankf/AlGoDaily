"""
    1st: sort + hashtable
    - sort the array
    - if the current word is a single character, put that in hashset
    - if the prefix of current word is in the hashset, put that in hashset
    - the longest key in hashset is the result

    Time    O(NlogN) n: number of words, k: average number of characters in words
    Space   O(N)
    76 ms, faster than 75.63%
"""


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(key=lambda w: len(w))
        hs = set()
        for w in words:
            if len(w) == 1 or w[:-1] in hs:
                hs.add(w)
        res = ''
        for w in hs:
            if len(w) > len(res):
                res = w
            elif len(w) == len(res) and w < res:
                res = w
        return res


a = ["w", "wo", "wor", "worl", "world"]
print(Solution().longestWord(a))

a = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(Solution().longestWord(a))

a = ["a"]
print(Solution().longestWord(a))

a = []
print(Solution().longestWord(a))

a = ["m", "mo", "moc", "moch", "mocha", "l", "la",
     "lat", "latt", "latte", "c", "ca", "cat"]
print(Solution().longestWord(a))
