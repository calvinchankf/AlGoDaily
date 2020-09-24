import sys
"""
    questions to ask:
    - upper case == lower case? yes
    - if there is a tie, return the first one? yes
"""

"""
    1st approach: hashtable
    Time    O(L+WK)
    Space   O(K)
    76 ms, faster than 55.30%
"""


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        licensePlate = licensePlate.lower()
        structure = 26 * [0]
        for c in licensePlate:
            if c.isalpha():
                structure[ord(c)-ord('a')] += 1
        resultLength = sys.maxsize
        result = ""
        for word in words:
            tempStruct = 26 * [0]
            for c in word:
                tempStruct[ord(c)-ord('a')] += 1
            found = True
            for i in range(26):
                if tempStruct[i] < structure[i]:
                    found = False
                    break
            if found and len(word) < resultLength:
                resultLength = len(word)
                result = word
        return result
