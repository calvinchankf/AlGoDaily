def solve(s):

    def f(s, fromIdx, ht):
        if fromIdx == len(s):
            return 1
        if fromIdx + 1 == len(s):
            if int(s[fromIdx]) == 0:
                return 0
            return 1
        else:
            if fromIdx in ht:
                return ht[fromIdx]

            a = s[fromIdx]
            b = s[fromIdx+1]
            c = int(a + b)

            if int(a) == 0:
                return 0

            ways1, ways2 = 0, 0

            if c <= 26:
                ways1 = f(s, fromIdx + 1, ht)
                ways2 = f(s, fromIdx + 2, ht)
            else:
                ways1 = f(s, fromIdx + 1, ht)

            ht[fromIdx] = ways1 + ways2
            return ht[fromIdx]

    return f(s, 0, {})


t = int(input())  # read a line with a single integer
for _ in range(t):
    n = input().strip()
    s = input().strip()
    res = solve(s)
    print(res)


a = '123'
print(f(a, 0, {}))

print("-----")

a = '2563'
print(f(a, 0, {}))

print("-----")

a = '226'
print(f(a, 0, {}))
