"""
    You are given an array a = [8, 9 , 10 , 0] with max value k

    All values in array have this property 0 <= value <= k
    You have to sort this array in ascending order a = [0, 8, 9, 10]

    Allowed unlimited space complexity. Use k as your advantage.
"""


def sortArray(nums, k):
    counter = {}
    for x in nums:
        if x not in counter:
            counter[x] = 0
        counter[x] += 1
    res = []
    for x in range(k+1):
        if x not in counter:
            continue
        res += [x] * counter[x]
    return res


a = [8, 9, 10, 0]
b = 10
print(sortArray(a, b))

a = [8, 8, 8, 9, 10, 10, 0]
b = 10
print(sortArray(a, b))
