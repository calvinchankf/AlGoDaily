# code
def f(pairs):
    intvs = sorted(pairs, key=lambda x: x[1])
    count = 0
    pos = -2**31
    for s, e in intvs:
        if s >= pos:
            pos = e
            count += 1
    return count


a = [
    [1, 3],
    [3, 4],
    [2, 6],
    [5, 7],
    [8, 9],
    [5, 9]
]
print(f(a))

a = [
    [1, 2],
    [3, 4],
    [2, 3],
    [5, 6]
]
print(f(a))

t = int(input())  # read a line with a single integer
for i in range(t):
    n = int(input())
    s = input().strip()
    e = input().strip()
    starts = [int(c) for c in s.split(" ")]
    ends = [int(c) for c in e.split(" ")]
    pairs = []
    for i in range(n):
        pairs.append([starts[i], ends[i]])
    print(f(pairs))
