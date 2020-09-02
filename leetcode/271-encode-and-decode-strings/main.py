"""
    1st approach: num sum
    - count the number of characters of each string and put it to the front of each string
        e.g. ['Hello', 'World'] -> 5>Hello5>World
    - when we see a [x], we regard the coming x characters as a string 

    Time    O(mn)
    Space   O(mn)
     332 ms, faster than 8.52%
"""


class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for s in strs:
            count = len(s)
            res += str(count) + '>' + s
        return res

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            num = 0
            while s[i] != '>':
                num = num * 10 + int(s[i])
                i += 1
            i += 1
            cur = ''
            for j in range(num):
                cur += s[i]
                i += 1
            res.append(cur)
        return res


e = Codec().encode(["Hello", "World"])
print(e)
d = Codec().decode(e)
print(d)


e = Codec().encode(["Hello", "World", ""])
print(e)
d = Codec().decode(e)
print(d)

e = Codec().encode(["_+{}:?(*&^", "", "", "World", "L}K::K"])
print(e)
d = Codec().decode(e)
print(d)
