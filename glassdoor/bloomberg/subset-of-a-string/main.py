"""
    https://leetcode.com/discuss/interview-question/439548/Bloomberg-Phone-Interview-Questions

    e.g. String "abc" should output
    empty string
    a
    b
    c
    ab
    bc
    ac
    abc
"""


def subsetsOfString(s):
    res = []

    def dfs(remain, chosen):
        res.append(chosen)
        for i in range(len(remain)):
            dfs(remain[i+1:], chosen+remain[i])
    dfs(s, '')

    return res


a = 'abc'
print(subsetsOfString(a))

a = 'wxyz'
print(subsetsOfString(a))
