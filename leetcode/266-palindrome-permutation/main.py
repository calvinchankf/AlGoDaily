from collections import Counter

"""
    1st approach: hashtable
    - for a valid palindrome, 
    the occurence of a number can only be even or there is only one odd occurence number

    Time    O(n)
    Space   O(n)
    20 ms, faster than 98.91%
"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter = Counter(s)
        oddCount = 0
        for key in counter:
            if counter[key] % 2 == 1:
                oddCount += 1
        return oddCount <= 1


"""
    2nd approach: ascii characters array
    - for a valid palindrome, 
    the occurence of a number can only be even or there is only one odd occurence number

    Time    O(n)
    Space   O(1) the seen array has only 128 slots
    20 ms, faster than 73.67%
"""


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        seens = 128*[0]
        for c in s:
            seens[ord(c)] += 1

        hasOdd = False
        for seen in seens:
            if seen % 2 > 0:
                if hasOdd == True:
                    return False
                hasOdd = True
        return True
