"""
    There is a string which only contains 0, 1 and '?', where, ? can be 0 or 1

    Given a string s, print all the possibilities.

    e.g.
    Input: '??01'
    Output: ['0001', '0101', '1001', '1101']
"""


def xx01(s):
    res = []

    def dfs(i, cur):
        if i == len(s):
            res.append(cur)
            return
        if s[i] == '?':
            dfs(i+1, cur + '0')
            dfs(i+1, cur + '1')
        else:
            dfs(i+1, cur+s[i])
    dfs(0, '')

    return res


a = '??01'
print(xx01(a))

a = '??0?1'
print(xx01(a))

print("-----")


def xx01(s):
    res = []
    q = [(0, '')]
    while len(q) > 0:
        i, cur = q.pop(0)
        if i == len(s):
            res.append(cur)
            continue
        if s[i] == '?':
            q.append((i+1, cur + '0'))
            q.append((i+1, cur + '1'))
        else:
            q.append((i+1, cur+s[i]))
    return res


a = '??01'
print(xx01(a))

a = '??0?1'
print(xx01(a))
