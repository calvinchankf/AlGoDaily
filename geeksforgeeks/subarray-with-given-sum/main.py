def f(nums, k):
    j = 0
    windowSum = 0
    for i in range(len(nums)):
        windowSum += nums[i]
        while windowSum > k:
            windowSum -= nums[j]
            j += 1
        if windowSum == k:
            return [j+1, i+1]
    return [-1]


t = int(input())  # read a line with a single integer
for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    n, k = [int(c) for c in s1.split(" ")]
    nums = [int(c) for c in s2.split(" ")]
    res = f(nums, k)
    print(' '.join([str(x) for x in res]))

"""
3
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
2 1
10 11
"""
