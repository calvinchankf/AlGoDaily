"""
    1st: array

    Time    O(N)
    Space   O(1)
    40 ms, faster than 100.00%
"""


class Solution(object):
    def reorderSpaces(self, text):
        words = text.split()
        spaces = 0
        for x in text:
            if x == ' ':
                spaces += 1

        if spaces == 0:
            return text

        if len(words) == 1:
            return words[0] + spaces * ' '

        d = spaces//(len(words) - 1)
        m = spaces % (len(words) - 1)

        res = ''
        for i in range(len(words)):
            if i + 1 == len(words):
                res += words[i] + m * ' '
            else:
                res += words[i] + d * ' '
        return res


s = Solution()

a = "  this   is  a sentence "
print(s.reorderSpaces(a))

a = " practice   makes   perfect"
print(s.reorderSpaces(a))

a = "hello   world"
print(s.reorderSpaces(a))

a = "  walks  udp package   into  bar a"
print(s.reorderSpaces(a))

a = "a"
print(s.reorderSpaces(a))

a = "  hello"
print(s.reorderSpaces(a))

a = "hello  "
print(s.reorderSpaces(a))
