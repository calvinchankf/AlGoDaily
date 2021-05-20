"""
    1st: 2 pointers
    - similar to lc3
    - if the current character cannot be appended to the end, discontinue
    - compare the length of every valid substring

    Time    O(N)
    Space   O(1)
    1056 ms, faster than 100.00%
"""


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        j = 0
        cur = ''
        order = {'': 0, 'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
        for i in range(len(word)):
            c = word[i]
            if c not in 'aeiou':
                j, cur = i+1, ''
                cur = ''
                continue
            if order[c] < order[cur] or order[c] > order[cur] + 1:
                if c == 'a':
                    j, cur = i, 'a'
                else:
                    j, cur = i+1, ''
                continue
            cur = c
            if c == 'u':
                res = max(res, i - j + 1)
        return res
