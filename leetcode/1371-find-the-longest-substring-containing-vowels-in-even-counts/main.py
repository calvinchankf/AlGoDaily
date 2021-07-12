"""
    1st: prefixSum + hashtable + bit op
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
    - then we can use the concept of lc560 to find out the longest subarray
    
    ref:
    - https://www.youtube.com/watch?v=tAlQxFvak2U

    Time    O(5N)
    Space   O(32*5)
    740 ms, faster than 22.90%
"""


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        ht = {
            (0, 0, 0, 0, 0): -1
        }
        curState = [0, 0, 0, 0, 0]
        res = 0
        for i in range(len(s)):
            j = 'aeiou'.find(s[i])
            if j >= 0:
                curState[j] ^= 1
            key = tuple(curState)
            if key not in ht:
                ht[key] = i
            res = max(res, i - ht[key])
        return res


"""
    2nd: optimized the 1st using a single number as a key

    Time    O(5N)
    Space   O(32)
    596 ms, faster than 35.00%
"""


class Solution(object):
    def findTheLongestSubstring(self, s: str) -> int:
        ht = {0: -1}
        curState = 0
        res = 0
        for i in range(len(s)):
            j = 'aeiou'.find(s[i])
            if j >= 0:
                curState ^= 1 << j
            if curState not in ht:
                ht[curState] = i
            res = max(res, i - ht[curState])
        return res
