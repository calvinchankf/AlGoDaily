from collections import Counter
import re

"""
    Questions to ask:
    - will there be numbers in a word? e.g. abs4sf?
    - does banned list contain a word having punctuation? abs4sf?
    - if a word is attached to any punctuation, e.g. bob's, should we count bob?
    - will the banned list be empty?
    - will the paragraph be emoty?
"""


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str

        1st approach
        1. put the banned words into a hashtable
        2. count the occurence of each word in the paragraph if it is not banned
        3. find the most freq word
        - takeaway: re.split(r'\W+', paragraph)
        Time    O(n)
        Space   O(n)
        24ms beats 98.2%
        """
        banned_set = set(banned)
        words = re.split(r'\W+', paragraph)
        ht = {}
        for word in words:
            w = word.lower()
            if w in banned_set or w == "":
                continue
            if w in ht:
                ht[w] += 1
            else:
                ht[w] = 1
        res_cnt = 0
        res = ""
        for key in ht:
            if ht[key] > res_cnt:
                res_cnt = ht[key]
                res = key
        return res


a = "Bob hit a  ball, the hit BALL flew far after it was hit."
print(Solution().mostCommonWord(a, ["hit"]))

a = "a, a, a, a, b,b,b,c, c"
print(Solution().mostCommonWord(a, ["a"]))

a = "Bob!"
print(Solution().mostCommonWord(a, ["hit"]))

print("------")


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banSet = set(banned)
        paragraph = paragraph.lower()
        words = re.split(r'\W+', paragraph)
        ht = Counter()
        maxCount = 0
        res = None
        for w in words:
            if len(w) == 0:
                continue
            if w in banSet:
                continue
            ht[w] += 1
            if ht[w] > maxCount:
                maxCount = ht[w]
                res = w
        return res


a = "Bob hit a  ball, the hit BALL flew far after it was hit."
print(Solution().mostCommonWord(a, ["hit"]))

a = "a, a, a, a, b,b,b,c, c"
print(Solution().mostCommonWord(a, ["a"]))

a = "Bob!"
print(Solution().mostCommonWord(a, ["hit"]))
