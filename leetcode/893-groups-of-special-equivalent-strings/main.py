"""
    1st: hashtable

    idea:
    zzxy -> xzzy -> xyzz
    - -     - -     - -

    Since we can swap the charactors arbitrarily at even indices, 'x' and 'z' are always at even indices
    even: xz
    odd:  zy <- same as odd indices

    So we can just build a key with the above 'even' and 'odd' for every string,
    put it in a hashset, then the size of hashset is the result

    Time    O(NK) N = number of strings, K = average length of string
    Space   O(N)
    44 ms, faster than 39.36%
"""


class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        hs = set()
        for s in A:
            key = self.getKey(s)
            hs.add(key)
        return len(hs)

    def getKey(self, s):
        odd = 26 * [0]
        even = 26 * [0]
        for i in range(len(s)):
            j = ord(s[i]) - ord('a')
            if i % 2 == 0:
                even[j] += 1
            else:
                odd[j] += 1
        return (tuple(odd), tuple(even))
