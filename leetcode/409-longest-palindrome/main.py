from collections import Counter
"""
    1st approach: hashtable
    1. count the occurence of each character
    2. make sure the all characters occurr "evenly" by declementing the odd ocurrence characters
    3. if no of odd ocurrence characters > 0, 
        wit means that we have to place any one of them in the center to form the biggest palindrome

    Time    O(N)
    Space   O(N)
    20 ms, faster than 85.04%
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        res = 0
        oddCount = 0
        for c in counter:
            if counter[c] % 2 == 0:
                res += counter[c]
            else:
                res += counter[c] - 1
                oddCount += 1
        if oddCount > 0:
            return res + 1
        return res


s = Solution()

a = "abccccdd"
print(s.longestPalindrome(a))

a = "aaaabbbccccddd"
print(s.longestPalindrome(a))

print("-----")
