def f(arr):
    maxNum = max(arr)
    dp = [0, 1]
    for i in range(2, maxNum+1):
        dp.append(dp[i-2] + dp[i-1])
    fibs = set(dp)
    res = []
    for x in arr:
        if x in fibs:
            res.append(str(x))
    print(' '.join(res))


a = [1, 4, 3, 9, 10, 13, 7]
print(f(a))

a = [0, 2, 8, 5, 2, 1, 4, 13, 23]
print(f(a))

t = int(input())  # read a line with a single integer
for i in range(t):
    k = input()
    s = input().strip()
    arr = [int(x) for x in s.split(" ")]
    f(arr)
