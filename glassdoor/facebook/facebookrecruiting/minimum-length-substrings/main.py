from collections import Counter

"""
    You are given two strings s and t. 
    You can select any substring of string s and rearrange the characters of the selected substring. 
    Determine the minimum length of the substring of s such that string t is a substring of the selected substring.

    Example 1
    s = "dcbefebce"
    t = "fd"
    output = 5
    Explanation:
    Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. String t is a substring of "cfdeb". Thus, the minimum length required is 5.

    Example 2
    s = "dcbefebce"
    t = "fx"
    output = -1

    Example 3
    s = "acfcfcdcff"
    t = "ffd"'
    output = 4
    Both substrings 'fcfcd' and 'dcff', result is 4 because 'dcff' is shorter
"""


"""
    - similar to lc3 but we need to check the frequency of a character from the left

    Time    O(26N)
    Space   O(26+26)
"""


def min_length_substring(s, t):
    target = 26 * [0]
    for c in t:
        i = ord(c) - ord('a')
        target[i] += 1
    cur = 26 * [0]
    j = 0
    res = 2**32
    for i in range(len(s)):
        c = s[i]
        idx = ord(c) - ord('a')
        cur[idx] += 1
        while True:
            left = s[j]
            idx = ord(left) - ord('a')
            if cur[idx] > target[idx]:
                j += 1
                cur[idx] -= 1
            else:
                break
        if ifContain(cur, target):
            res = min(res, i - j + 1)
    if res == 2**32:
        return -1
    return res


def ifContain(cur, target):
    for i in range(26):
        if cur[i] < target[i]:
            return False
    return True


# 5
a = 'dcbefebce'
b = 'fd'
print(min_length_substring(a, b))

# -1
a = 'bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf'
b = 'cbccfafebccdccebdd'
print(min_length_substring(a, b))

# 4
a = 'acfcfcdcff'
b = 'ffd'
print(min_length_substring(a, b))
