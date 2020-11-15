from collections import *

"""
    1st approach: hashtable
    - count the occurence, N, of each character and put the count in a hashtable
    - for each c in S, if c is in the hashtable, append the N*"c" in the result string and remove c from the hashtbale
    - for the remaining characters in the hashtable, put them back to the result string

    Time    O(S+T)
    Space   O(T)
    20 ms, faster than 58.70%
"""


class Solution(object):
    def customSortString(self, S, T):
        # count the occurence, N, of each character and put the count in a hashtable
        counter = Counter(T)
        # for each c in S, if c is in the hashtable,
        # append the N*"c" in the result string and remove c from the hashtbale
        res = ''
        for c in S:
            if c in counter:
                count = counter[c]
                res += count * c
                del counter[c]
        # for the remaining characters in the hashtable, put them back to the result string
        for c in counter:
            count = counter[c]
            res += count * c
        return res


a = "kqep"
b = "pekeq"
print(Solution().customSortString(a, b))

a = "cba"
b = "abeabfcd"
print(Solution().customSortString(a, b))

"""
    followup: for the characters not in S, append them to the result string by insertion order

    Time    O(S+T)
    Space   O(T)
    12 ms, faster than 99.67%
"""


class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # count the occurence, N, of each character and put the count in a hashtable
        m = OrderedDict()
        for c in T:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        # for each c in S, if c is in the hashtable,
        # append the N*"c" in the result string and remove c from the hashtbale
        res = ""
        for c in S:
            if c in m:
                res += m[c] * c
                del m[c]
        # for the remaining characters in the hashtable, put them back to the result string
        for key in m:
            res += m[key] * key

        return res


a = "kqep"
b = "pekeq"
print(Solution().customSortString(a, b))

a = "cba"
b = "abeabfcd"
print(Solution().customSortString(a, b))
