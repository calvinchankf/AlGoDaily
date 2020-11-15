# code
def f(arr, k):
    j = 0
    windowSum = 0
    resSum = 2**32
    res = len(arr)
    for i in range(len(arr)):
        windowSum += arr[i]
        while windowSum > k:
            if i - j + 1 < res:
                resSum = windowSum
                res = i - j + 1
            windowSum -= arr[j]
            j += 1
    return resSum, res


a = [1, 4, 45, 6, 0, 19]
b = 51
print(f(a, b))

a = [1, 10, 5, 2, 7]
b = 9
print(f(a, b))

a = [178, 116, 294, 236, 287, 193, 250, 122, 63, 128, 291, 260, 264, 227, 241, 127,
     173, 137, 12, 69, 268, 130, 183, 231, 63, 224, 68, 236, 30, 103, 223, 259, 270, 268]
b = 387
print(f(a, b))


t = int(input())  # read a line with a single integer
for i in range(t):
    s1 = input().strip()
    s2 = input().strip()
    n, k = [int(c) for c in s1.split(" ")]
    arr = [int(c) for c in s2.split(" ")]
    _, res = f(arr, k)
    print(res)
