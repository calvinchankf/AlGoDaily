# https://leetcode.com/discuss/interview-question/357345/Facebook-or-Phone-Screen-or-Sum-to-100

res = []

# yo = {'count': 0}


def dfs(s, path, total):
    # yo['count'] += 1
    # print(path)

    if len(s) == 0:
        if total == 100:
            res.append(path)
        return
    for i in range(1, len(s) + 1):
        dfs(s[i:], path + '+' + s[:i], total + int(s[:i]))
        dfs(s[i:], path + '-' + s[:i], total - int(s[:i]))


dfs('123', '', 0)

print(res)
# print(yo['count'])


"""
Time    O(3^9) but it is hard to come up with

                    9*2 = 18
8*2 = 16, 7*2 = 14, 6*2 = 12....
7*2 = 14...

result: 
[
    '+1+2+3-4+5+6+78+9',
    '+1+2+34-5+67-8+9',
    '+1+23-4+5+6+78-9',
    '+1+23-4+56+7+8+9',
    '-1+2-3+4+5+6+78+9',
    '+12+3+4+5-6-7+89',
    '+12+3-4+5+67+8+9',
    '+12-3-4+5-6+7+89',
    '+123+4-5+67-89',
    '+123-4-5-6-7+8-9',
    '+123+45-67+8-9',
    '+123-45-67+89',
]
"""
