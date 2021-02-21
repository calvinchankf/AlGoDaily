"""
    1st approach
	1. reverse the whole string
	2. iterate forward, reverse a word in the back if encounter a space/end of a string
    
	Time	O(n) 2n->n
	Space	O(1) in-place
	264 ms, faster than 52.17%
"""


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        n = len(s)
        self.reverse(s, 0, n-1)
        slow = 0
        for i in range(n):
            if i+1 == n:
                self.reverse(s, slow, i)
            elif s[i] == ' ':
                self.reverse(s, slow, i-1)
                slow = i + 1

    def reverse(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
