"""
    1st: 2 pointers
    - very annoyong implementation

    ref:
    - https://www.youtube.com/watch?v=GqXlEbFVTXY

    Time    O(WM)
    Space   O(WM)
    40 ms, faster than 10.02%
"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        while i < len(words):
            j = i + 1
            curLen = len(words[i])
            while j < len(words) and curLen + len(words[j]) + (j - i) <= maxWidth:
                curLen += len(words[j])
                j += 1
            wordsCount = j - i
            spacesCount = maxWidth - curLen
            if j == len(words) or wordsCount == 1:
                temp = self.leftJustify(words, i, j, maxWidth)
                res.append(temp)
            else:
                temp = self.middleJustify(words, i, j, spacesCount)
                res.append(temp)
            i = j
        return res

    def leftJustify(self, words, i, j, maxWidth):
        res = words[i]
        for k in range(i+1, j):
            res += ' ' + words[k]
        res += ' ' * (maxWidth - len(res))
        return res

    def middleJustify(self, words, i, j, spacesCount):
        gapsCount = j - i - 1
        spaces = spacesCount // gapsCount
        extraSpaces = spacesCount % gapsCount
        res = words[i]
        for k in range(i+1, j):
            spacesToApply = spaces + (1 if extraSpaces > 0 else 0)
            extraSpaces -= 1
            res += ' ' * spacesToApply + words[k]
        return res


s = Solution()

a = ["This", "is", "an", "example", "of", "text", "justification."]
b = 16
print(s.fullJustify(a, b))

a = ["What", "must", "be", "acknowledgment", "shall", "be"]
b = 16
print(s.fullJustify(a, b))

a = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
     "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
b = 20
print(s.fullJustify(a, b))
