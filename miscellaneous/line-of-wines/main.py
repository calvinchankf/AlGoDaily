"""
    There are N wines in a row. Each year you sell either wine at the leftmost OR the rightmost position.
    The i-th wine has and initial price[i] and the price would raise according to the number years,
    e.g. price = 4
    1st year: price = 1*4 = 4
    2nd year: price = 2*4 = 8
    3rd year: price = 3*4 = 12
    ...
    What is the maximum possible profit you can have after N years

    e.g. [2, 4, 6, 2, 5]
    result = 1*2 + 2*5 + 3*2 + 4*4 + 5*6 = 64

    Time    O(N^2)
    Space   O(N^2)
"""
def lineOfWines(nums):
    return dfs(nums, 0, len(nums)-1, 1, {})

def dfs(nums, i, j, k, ht):
    if i == j:
        return k * nums[i]
    key = (i, j)
    if key in ht:
        return ht[key]
    left = dfs(nums, i+1, j, k+1, ht) + k*nums[i] 
    right = dfs(nums, i, j-1, k+1, ht) + k*nums[j]
    ht[key] = max(left, right)
    return ht[key]

a = [2, 4, 6, 2, 5]
print(lineOfWines(a))

a = [2, 4, 6, 2, 5, 4, 1, 6, 8, 9, 6, 3, 4, 2, 4, 6, 2, 5, 4, 1, 6, 8, 9, 6, 3, 4]
print(lineOfWines(a))