from collections import *

"""
    1st: hashtable

    approach for operation 1:
    - as long as they are anagram, we can swap any number of times to make them equal
   
    approach for operation 2:
    - as long as the chars-frequency of S and T are the same, we can swap the frequencies any number of times to make them equal

    Time     O(SlogS + TlogT)
    Space    O(S+T)
    560 ms, faster than 34.78% 
"""


class Solution(object):
    def closeStrings(self, word1, word2):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        # for op1
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        for i in range(26):
            key = alphabets[i]
            if key in counter1 and key not in counter2:
                return False
            if key in counter2 and key not in counter1:
                return False
        # for op2
        nums1 = sorted([counter1[k] for k in counter1])
        nums2 = sorted([counter2[k] for k in counter2])
        return tuple(nums1) == tuple(nums2)


"""
    2nd: hashtables
    - simlar to 1st but use a hashtable to speed up

    Time     O(S+T)
    Space    O(S+T)
    560 ms, faster than 34.78% 
"""


class Solution(object):
    def closeStrings(self, word1, word2):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        for i in range(26):
            key = alphabets[i]
            if key in counter1 and key not in counter2:
                return False
            if key in counter2 and key not in counter1:
                return False
        freqs = Counter([counter1[k] for k in counter1])
        for x in counter2.values():
            if x in freqs:
                freqs[x] -= 1
                if freqs[x] == 0:
                    del freqs[x]
        return len(freqs) == 0
