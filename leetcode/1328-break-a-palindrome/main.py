from collections import defaultdict

"""
    1st: string
    - the basic idea is to find make the first character after 'a' to an 'a'
    - but there are some corner cases

    e.g.
    - aaaaaa -> aaaaab
    - aabaa -> aabab
    - a to z -> ''

    Time    O(N)
    Space   O(N)
    16 ms, faster than 74.73%
"""


class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) <= 1:
            return ""
        ht = defaultdict(int)
        for i in range(len(palindrome)):
            c = palindrome[i]
            ht[c] += 1

        keys = ht.keys()
        if (len(keys) == 1 and keys[0] == 'a'):
            return palindrome[:-1] + 'b'
        elif len(keys) == 2:
            a, b = keys[0], keys[1]
            if (a == 'a' and ht[b] == 1) or (b == 'a' and ht[a] == 1):
                return palindrome[:-1] + 'b'

        for i in range(len(palindrome)):
            c = palindrome[i]
            if c != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
