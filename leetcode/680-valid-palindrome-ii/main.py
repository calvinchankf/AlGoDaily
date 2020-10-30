"""
    0th: brute force
    Time    O(N^2) LTE
"""

"""
    2nd: 2 pointers trick on edit one distance
    - whenever there is an unmatch between s[left] and s[right], we check if the middle is a palindrome

    e.g.1. abxcdedcba

    abxcdedcba
      ^    ^     <- s[left] != s[right]
    so we should now check if either
    - cdedc 
    - xcded
    is a palindrome

    e.g.2. abcdedcxba
    abcdedcxba
      ^    ^     <- s[left] != s[right]
    same logic applies

    Time    O(N)
    Space   O(1)
    168 ms, faster than 57.50%
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        i = 0
        j = n - 1
        while i <= j:
            if s[i] != s[j]:
                a = self.isPalindrome(s[i:j])
                b = self.isPalindrome(s[i+1:j+1])
                return a or b
            i += 1
            j -= 1
        return True
    
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True