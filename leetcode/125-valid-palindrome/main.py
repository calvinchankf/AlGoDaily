"""
    1st approach: classic approach
	- 2 pointers: 1 from the front, 1 from the back, and check if s[i] == s[j]

	Time		O(n)
	Space		O(1)
	4 ms, faster than 96.94%
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
        while left <= right:
            if self.isAlphanumeric(s[left]) and self.isAlphanumeric(s[right]):
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            elif self.isAlphanumeric(s[left]):
                right -= 1
            elif self.isAlphanumeric(s[right]):
                left += 1
            else:
                left += 1
                right -= 1

        return True

    def isAlphanumeric(self, s):
        if (ord(s) >= 65 and ord(s) <= 90) \
                or (ord(s) >= 97 and ord(s) <= 122) \
                or (ord(s) >= 48 and ord(s) <= 57):
            return True
        return False


"""
    2nd: similar to 1st but concise

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
