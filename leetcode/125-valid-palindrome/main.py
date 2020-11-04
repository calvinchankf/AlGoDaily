"""
    1st: classic approach
	- 2 pointers: 1 from the front, 1 from the back, and check if s[i] == s[j]

    Time    O(N)
    Space   O(1)
    52 ms, faster than 47.60%
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            while left < right and not self.isAlphanumeric(s[right]):
                right -= 1
            if left <= right and s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def isAlphanumeric(self, c):
        return 0 <= ord(c) - ord('a') < 26 or 0 <= ord(c) - ord('0') < 10


"""
    2nd: similar to 1st but concise

    Time    O(N)
    Space   O(1)
    48 ms, faster than 68.75%
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        i = 0
        j = n - 1
        while i <= j:
            while i+1 <= j and s[i].isalnum() == False:
                i += 1
            while j-1 >= i and s[j].isalnum() == False:
                j -= 1
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True