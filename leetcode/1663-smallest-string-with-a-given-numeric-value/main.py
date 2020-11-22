"""
    2nd: greedy
    
    e.g. n = 5, k = 73
    
    1. initialize an array of As
    res = 'aaaaa'       <= temporary result    
    k   = 73-5 = 68     <= k subtracts n because it spent 5 units

    2. now we try to allocate Zs as many as possible
    68-25 = 43, res = 'aaaaz'
    43-25 = 18, res = 'aaazz'
    18-18 = 0,  res = 'aaszz'

    Time    O(N)
    Space   O(26)
    432 ms, faster than 50.00%
"""


class Solution(object):
    def getSmallestString(self, n: int, k: int) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        res = n * ['a']
        k -= n
        i = n - 1
        while k > 0:
            charIdx = min(25, k)
            res[i] = alphabets[charIdx]
            k -= charIdx
            i -= 1
        return ''.join(res)
