def f(s):
    res = int(s[0])
    for i in range(1, len(s)):
        cur = int(s[i])
        res = max(res * cur, res + cur)
    return res


a = '01230'
print(f(a))

a = '891'
print(f(a))

t = int(input())  # read a line with a single integer
for _ in range(t):
    s = input().strip()
    res = f(s)
    print(res)
