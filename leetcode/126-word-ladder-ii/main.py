import sys
from collections import defaultdict

"""
    1st approach: BFS + hashset
    - similar to lc127

    LTE 19 / 39 test cases passed.
"""


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)  # avoid duplicate words
        # BFS
        q = []
        q.append((beginWord, [beginWord], set()))
        # seen = set()  # avoid revisting a seen word
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        temps = []
        shortest = len(wordList)
        while len(q) > 0:
            word, path, seen = q.pop(0)
            if word == endWord:
                if len(path) < shortest:
                    shortest = len(path)
                temps.append(path)
            if len(path) > len(wordList):
                break
            # explore at index=0 hit => ait, bit, cit....
            # explore at index=1 hit => hat, hbt, hct....
            for i in range(len(word)):
                for c in alphabets:
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordList and newWord not in seen:
                        newSet = set(seen)
                        newSet.add(newWord)
                        q.append((newWord, path + [newWord], newSet))
                        seen.add(newWord)
        res = []
        for temp in temps:
            if len(temp) == shortest:
                res.append(temp)
        return res


s = Solution()

a = "abc"
b = "ade"
c = ["abd", "azd", "add", "ade"]
print(s.findLadders(a, b, c))

a = "hit"
b = "cog"
c = ["hot", "dot", "dog", "lot", "log", "cog"]
print(s.findLadders(a, b, c))

a = "hit"
b = "cog"
c = ["hot", "dot", "dog", "lot", "log"]
print(s.findLadders(a, b, c))

a = "leet"
b = "code"
c = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
print(s.findLadders(a, b, c))

a = "qa"
b = "sq"
c = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb",
     "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]
# print(s.findLadders(a, b, c))

print("-----")

"""
    2nd: optimize the 1st approach
    - cache all the combinations of words that can be formed, e.g. { '*ot': ['hot', 'dot', 'lot'], 'do*': ['dot', 'dog']...etc}
    - bfs

    Time    O(N^26*wordLength) ???
    Space   O(N)
    308 ms, faster than 80.18%
"""


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        L = len(beginWord)
        # a dictionary to gather all combinations of words that can be formed
        # e.g. { '*ot': ['hot', 'dot', 'lot'], 'do*': ['dot', 'dog']...etc}
        combos = defaultdict(list)
        for word in wordList:
            for i in range(L):
                combos[word[:i] + "*" + word[i+1:]].append(word)
        # bfs
        ans = []
        q = [(beginWord, [beginWord])]
        seen = set([beginWord])
        while q and not ans:
            n = len(q)
            lcoalSeen = set()
            # only process the nodes on the same level
            for _ in range(n):
                word, path = q.pop(0)
                for i in range(L):
                    for nextWord in combos[word[:i] + "*" + word[i+1:]]:
                        if nextWord == endWord:
                            ans.append(path+[endWord])
                        if nextWord not in seen:
                            lcoalSeen.add(nextWord)
                            q.append((nextWord, path+[nextWord]))
            seen = seen.union(lcoalSeen)
        return ans


s = Solution()

a = "abc"
b = "ade"
c = ["abd", "azd", "add", "ade"]
print(s.findLadders(a, b, c))

a = "hit"
b = "cog"
c = ["hot", "dot", "dog", "lot", "log", "cog"]
print(s.findLadders(a, b, c))

a = "hit"
b = "cog"
c = ["hot", "dot", "dog", "lot", "log"]
print(s.findLadders(a, b, c))

a = "leet"
b = "code"
c = ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
print(s.findLadders(a, b, c))

a = "qa"
b = "sq"
c = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb",
     "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]
print(s.findLadders(a, b, c))
