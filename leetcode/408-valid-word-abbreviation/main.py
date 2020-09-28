"""
    1st approach: brute force
    - contruct a string from abbr
    - compare word with that string

    e.g. s = internationalization, abbr = i12iz4n

    s    => internationalization
    abbr => i____________iz____n


    Time    O(n)
    Space   O(n)
    32 ms, faster than 12.99%
"""


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        s = ''
        num = 0
        for c in abbr:
            if c.isdigit():
                if num == 0 and int(c) == 0:
                    return False
                num = num*10 + int(c)
            else:
                if num > 0:
                    s += num * '#'
                    num = 0
                s += c
        if num >= 999999999:
            return False
        if num > 0:
            s += num * '#'
            num = 0
        if len(s) != len(word):
            return False
        for i in range(len(word)):
            if s[i] != '#' and word[i] != s[i]:
                return False
        return True


a = 'internationalization'
b = 'i12iz4n'
print(Solution().validWordAbbreviation(a, b))

a = 'apple'
b = 'a2e'
print(Solution().validWordAbbreviation(a, b))

a = 'a'
b = '01'
print(Solution().validWordAbbreviation(a, b))

a = 'bignumberhahaha'
b = '999999999'
print(Solution().validWordAbbreviation(a, b))

print("-----")

"""
    2nd approach: 2 pointers
    - one pointer to iterate 'word'
    - another pointer to iterate 'abbr'
    - when we see a number in abbr, move the word pointer forward with that number
    - return true if both pointers finally reach to the end

    e.g. s = internationalization, abbr = i12iz4n

    
    internationalization, i12iz4n
    ^                     ^
    i=0                   j=0

    internationalization, i12iz4n
                 ^           ^
            i=1+12=13       j=3
    
    internationalization, i12iz4n
                  ^           ^
            i=1+12=14       j=4
    
    internationalization, i12iz4n
                       ^        ^
                i=15+4=19       j=6
    
    internationalization, i12iz4n
                        ^        ^
                        end     end

    Time    O(n)
    Space   O(1)
    32 ms, faster than 12.99%
    20 ms, faster than 73.62% 
"""


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit() == False:
                return False
            else:
                if abbr[j] == '0':
                    return False
                num = int(abbr[j])
                while j+1 < len(abbr) and abbr[j+1].isdigit():
                    j += 1
                    num = num * 10 + int(abbr[j])
                i += num
                j += 1
        return i == len(word) and j == len(abbr)


a = 'internationalization'
b = 'i12iz4n'
print(Solution().validWordAbbreviation(a, b))

a = 'apple'
b = 'a2e'
print(Solution().validWordAbbreviation(a, b))

a = 'a'
b = '01'
print(Solution().validWordAbbreviation(a, b))

a = 'bignumberhahaha'
b = '999999999'
print(Solution().validWordAbbreviation(a, b))
