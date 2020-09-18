from collections import Counter
"""
    1st approach: hashtable
    1. count the occurence of each character
    2. make sure the all characters occurr "evenly" by declementing the odd ocurrence characters
    3. if no of odd ocurrence characters > 0, 
        wit means that we have to place any one of them in the center to form the biggest palindrome

    Time    O(n)
    Space   O(n)
    36 ms, faster than 15.64%
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        # count the occurence of each character
        ht = {}
        for c in s:
            if c in ht:
                ht[c] += 1
            else:
                ht[c] = 1

        # make sure the all characters occurr "evenly"
        noOfOdd = 0
        res = len(s)
        for key in ht:
            if ht[key] % 2 != 0:
                res -= 1
                noOfOdd += 1

        # if no of odd ocurrence characters > 0, it means that we have to place any one of them in the center to form the biggest palindrome
        if noOfOdd > 0:
            res += 1
        return res


s = Solution()

a = "abccccdd"
print(s.longestPalindrome(a))

a = "aaaabbbccccddd"
print(s.longestPalindrome(a))

print("-----")


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        largestOddCount = 0
        largestOdd = None
        for key in counter:
            if counter[key] % 2 == 1 and counter[key] > largestOddCount:
                largestOddCount = counter[key]
                largestOdd = key
        res = 0
        for key in counter:
            if counter[key] % 2 == 0:
                res += counter[key]
            else:
                if key == largestOdd:
                    res += counter[key]
                else:
                    res += counter[key] - 1
        return res


s = Solution()

a = "abccccdd"
print(s.longestPalindrome(a))

a = "aaaabbbccccddd"
print(s.longestPalindrome(a))
