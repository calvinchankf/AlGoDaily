"""
    greedy
    
    Time    O(N)
    Space   O(N)
    620 ms
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        res = n * ['a']
        for i in range(n-1, -1, -1):
            k -= i
            if k >= 0:
                if k < 26:
                    res[i] = alphabets[k-1]
                    k = 0
                else:
                    res[i] = 'z'
                    k -= 26
            else:
                continue
            k += i
        return ''.join(res)
