def f(nums, k):
    k = min(k, len(nums))
    nums = nums + nums
    res = 0
    windowSum = 0
    for i in range(len(nums)):
        windowSum += nums[i]
        if i >= k:
            windowSum -= nums[i-k]
        res = max(res, windowSum)
    return res % (10**9 + 7)


a = [2, 1, 3, 5, 0, 1, 4]
b = 3
print(f(a, b))

a = [1, 6, 2, 5, 3, 4]
b = 2
print(f(a, b))

a = [5, 7, 8, 5, 7, 0, 4, 7, 0]
b = 9
print(f(a, b))

a = [3, 8, 4, 7, 8, 9, 5, 0, 8]
b = 7
print(f(a, b))

a = [9, 0]
b = 7
print(f(a, b))

t = int(input())  # read a line with a single integer
for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    n, k = [int(c) for c in s1.split(" ")]
    nums = [int(c) for c in s2.split(" ")]
    res = f(nums, k)
    print(res)

"""
4
7 3
2 1 3 5 0 1 4
6 2
1 6 2 5 3 4
9 9
5 7 8 5 7 0 4 7 0 
9 7
3 8 4 7 8 9 5 0 8
"""
