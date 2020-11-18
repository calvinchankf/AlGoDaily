def f(A, B, target):
    res = []
    hs = set(A)
    for x in B:
        remain = target - x
        if remain in hs:
            res.append([remain, x])
    return sorted(res)


a = [1, 2, 4, 5, 7]
b = [5, 6, 3, 4, 8]
c = 9
print(f(a, b, c))

a = [0, 2]
b = [1, 3]
c = 3
print(f(a, b, c))

t = int(input())  # read a line with a single integer
for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    s3 = input().strip()
    _, _, target = [int(c) for c in s1.split(" ")]
    A = [int(c) for c in s2.split(" ")]
    B = [int(c) for c in s3.split(" ")]
    res = f(A, B, target)

    final = []
    for x, y in res:
        final.append(str(x) + ' ' + str(y))
    if len(final) == 0:
        print(-1)
    else:
        print(', '.join(final))

"""
3
5 5 9
1 2 4 5 7
5 6 3 4 8
2 2 3
0 2
1 3
2 26 97
-1 2
-4 5 -7 -11 -17 -24 25 39 42 -43 44 -48 54 55 64 69 70 -72 82 -83 -86 -88 -90 -96 97 99
"""
