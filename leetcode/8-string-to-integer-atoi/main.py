"""
    1st approach
	- straight forward approach
	- be careful of the corner cases

	Time 	O(n) n=length of input string
	Space O(1)
	4ms beats 100%
	19may2019
"""


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0
        num = 0
        polarity = 0
        if s[0] == '+':
            polarity = 1
        elif s[0] == '-':
            polarity = -1
        elif s[0].isdigit():
            num = int(s[0])
        else:
            return 0

        for i in range(1, len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            else:
                break
        if polarity == -1:
            return self.bound(-num)
        return self.bound(num)

    def bound(self, num):
        if num < -2**31:
            return -2**31
        elif num > 2**31-1:
            return 2**31-1
        return num


s = Solution()

print(s.myAtoi('42'))
print(s.myAtoi('-42'))
print(s.myAtoi(' -42'))
print(s.myAtoi('4193 with words'))
print(s.myAtoi('words and 987'))
print(s.myAtoi('22 and 987'))
print(s.myAtoi(' -22 and 987'))
print(s.myAtoi(' -+22 and 987'))
print(s.myAtoi('-91283472332'))
print(s.myAtoi('-91283472332 a'))
print(s.myAtoi(' -91283472332'))
print(s.myAtoi(' -91283472332 a'))
print(s.myAtoi(' a-91283472332'))
print(s.myAtoi('00000-42a1234'))
