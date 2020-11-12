"""
    1st: stack + hashtable
    - similar to lc921 but save the indices of the redundant opens & closes
    - construct the result by removing the characters at redundant indices
    
    Time    O(2N)
    Space   O(N)
    164 ms, faster than 79.33%
"""


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        opens = []
        closes = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                opens.append(i)
            elif c == ')':
                if len(opens) > 0:
                    opens.pop()
                else:
                    closes.append(i)
        hs = set(opens + closes)
        res = ''
        for i in range(len(s)):
            c = s[i]
            if i not in hs:
                res += c
        return res


"""
    2nd: similar logic

    takeaway: add list to a set()
    https://docs.python.org/3/library/stdtypes.html#frozenset.update

    Time    O(2N)
    Space   O(N)
    188 ms, faster than 61.42%
"""


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        redundant = set()
        opens = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                opens.append(i)
            elif c == ')':
                if len(opens) == 0:
                    redundant.add(i)
                else:
                    opens.pop()
        redundant |= set(opens)
        return ''.join(s[i] for i in range(len(s)) if i not in redundant)


"""
    3rd: similar logic without using a hashtable

    Time    O(3N)
    Space   O(N)
    244 ms, faster than 45.31%
"""


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        opens = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                opens.append(i)
                res += c
            elif c == ')':
                if len(opens) == 0:
                    res += '*'
                else:
                    opens.pop()
                    res += c
            else:
                res += c
        for x in opens:
            res[x] = '*'
        return ''.join(c for c in res if c != '*')
