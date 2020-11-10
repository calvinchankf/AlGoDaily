from collections import *


def f(arr, k):
    counter = Counter(arr)
    res = set()
    for i in range(len(arr)):
        x = arr[i]
        remain = k + x
        if remain in counter:
            if remain == x:
                if counter[x] > 1:
                    res.add((x, x))
            else:
                a = min(x, remain)
                b = max(x, remain)
                res.add((a, b))
    return list(res)


a = [1, 5, 4, 1, 2]
b = 0
print(f(a, b))

a = [1, 1, 1]
b = 0
print(f(a, b))

a = [1, 5, 3]
b = 2
print(f(a, b))

a = [1, 5, 3, 4, 2]
b = 3
print(f(a, b))

a = [8, 12, 16, 4, 0, 20]
b = 4
print(f(a, b))

a = [74, 3659, 8931, 1273, 7545, 879, 7924, 7710]
b = 50
print(f(a, b))

a = [5357, 9462, 8488, 8354, 3900, 5789, 4245, 9881, 2467, 8284,
     5275, 237, 8910, 8568, 1835, 7940, 9685, 9652, 9550, 9267]
b = 80
print(f(a, b))

t = int(input())  # read a line with a single integer
for i in range(t):
    n = input()
    s = input().strip()
    arr = [int(c) for c in s.split(" ")]
    k = int(input())
    res = f(arr, k)
    print(len(res))
