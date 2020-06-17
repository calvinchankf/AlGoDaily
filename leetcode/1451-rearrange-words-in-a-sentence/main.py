from collections import defaultdict

"""
    1st: hashtable
    - store a hashtable with key: value = length: array of words
    - sort the keys
    - construct the result

    Time    O(N + klogk)
    Space   O(N)
    56 ms, faster than 100.00%
"""


class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        text = text.lower()
        ht = defaultdict(list)
        for word in text.split(' '):
            length = len(word)
            ht[length].append(word)
        res = ''
        keys = ht.keys()
        keys.sort()
        for key in keys:
            arr = ht[key]
            res += ' '.join(arr) + ' '
        return res[0].upper() + res[1:-1]
