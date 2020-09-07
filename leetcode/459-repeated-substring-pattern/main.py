class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        1st approach: replace string
        - for each substring, check if the remaining string will be empty if we replace the substring with empty

        Time    O(n^2)
        Space   O(1)
        3604 ms, faster than 5.09%
        """
        for i in range(1, len(s)/2+1):
            sub = s[:i]
            if self.check(s[i:], sub) == True:
                return True
        return False

    def check(self, s, sub):
        x = s.replace(sub, "")
        return len(x) == 0


print(Solution().repeatedSubstringPattern("a"))
print(Solution().repeatedSubstringPattern("ab"))
print(Solution().repeatedSubstringPattern("aa"))
print(Solution().repeatedSubstringPattern("aaa"))
print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("ababa"))
print(Solution().repeatedSubstringPattern("abcabc"))
print(Solution().repeatedSubstringPattern("abccda"))


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        2nd approach: WTF
        e.g.1
        S = abcabc
        SS = bcabcabcab <= (S+S)[1:-1] stripe out the front and end
        check of S is in SS, bc|abcabc|ab <= return true

        e.g.2
        S = abcab
        SS = bcababca <= (S+S)[1:-1] stripe out the front and end
        check of S is in SS, return false

        Time	O(n)
        Space	O(n)
        20ms beats 100%
        """
        if not s:
            return False
        ss = (s + s)[1:-1]
        return ss.find(s) != -1


"""
    3rd: repeating substring to see if we can form our result string

    Time    O(N^2)
    Space   O(N)
    1096 ms, faster than 6.16%
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n-1):
            sub = s[:i+1]
            cur = ''
            while len(cur) < len(s):
                cur += sub
            if cur == s:
                return True
        return False
