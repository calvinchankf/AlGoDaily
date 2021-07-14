"""
    1st: prefixsum + hashtable + bit op
    - learned from others, this is not an easy medium
    - the idea is based on lc560
    - for every vowel, we dont need to know the exact number of times it appears, we just need to know it appears for even/odd number of times
    - we can use a tuple to represent the even/odd for 5 vowels
        e.g. (0, 1, 0, 1, 1) means
        a: even
        e: odd
        i: even
        o: odd
        u: odd
        when the curent character is a vowel, flip the bit
        e.g. (0, 1, 0, 1, 1) -> see an U -> (0, 1, 0, 1, 0)
    - since the characters are just from A to J, we can use 10bits to represent their even/odd
    
    Time    O(10N)
    Space   O(2^10=1024)
    2916 ms, faster than 55.75%
"""
from collections import Counter


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ht = {0: 1}
        curState = 0
        res = 0
        for i in range(len(word)):
            c = word[i]
            idx = ord(c) - ord('a')
            if idx >= 0:
                curState ^= 1 << idx

            # When we meet a state we have seen before, it means the substring characters have even frequency
            # i.e. it means the bits difference is 0
            if curState in ht:
                res += ht[curState]

            # For each bit, we try to cancel out it and see if there is a state we have seen before
            # If yes, it fulfills "at most one letter appears an odd number of times"
            # i.e. it means the bits difference is 1
            for j in range(10):
                newState = curState ^ (1 << j)
                if newState in ht:
                    res += ht[newState]

            if curState not in ht:
                ht[curState] = 0
            ht[curState] += 1
        return res


"""
    2nd: same as 1st but easier to implement

    Time    O(10N)
    Space   O(2^10=1024)
    4084 ms, faster than 18.08%
"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ht = Counter()
        ht[0] = 1
        curState = 0
        res = 0
        for i in range(len(word)):
            c = word[i]
            idx = ord(c) - ord('a')
            if idx >= 0:
                curState ^= 1 << idx

            res += ht[curState]

            for j in range(10):
                newState = curState ^ (1 << j)
                res += ht[newState]

            ht[curState] += 1
        return res
