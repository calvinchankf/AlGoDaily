"""
    classic and basic: max sum only


    You're given an array of arrays where each subarray holds two integer values
    and represents an item:
    - the first integer is the item's value
    - the secondinteger is the item's weight. 
    
    You're also given an integer representing the maximum capacity of a knapsack that you have.


    Your goal is to fit items in your knapsack without having the sum of their
    weights exceed the knapsack's capacity, all the while maximizing their
    combined value. Note that you only have one of each item at your disposal.

    Input:
    items = [[2, 1], [70, 70], [30, 30], [69, 69], [100, 100]]
    capacity = 100

    Output: 101 because sum of the items [0, 2, 3] = 101 and weight 100 in total
"""
def knapsackProblem(items, capacity):
    return dfs(items, 0, capacity, {})

def dfs(items, i, cap, ht):
	if i == len(items):
		return 0
	key = (i, cap)
	if key in ht:
		return ht[key]
	selected = 0
	if cap >= items[i][1]:
		selected = dfs(items, i+1, cap - items[i][1], ht) + items[i][0]
	notSelected = dfs(items, i+1, cap, ht)
	total = max(selected, notSelected)
	ht[key] = total
	return ht[key]


a = [[1, 2], [4, 3], [5, 6], [6, 7]]
b = 10
print(knapsackProblem(a, b)) # 10

a = [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [240, 40]
]
b = 200
print(knapsackProblem(a, b)) # 1500

a = [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [255, 40]
]
b = 200
print(knapsackProblem(a, b)) # 1505

a = [[2, 1], [70, 70], [30, 30], [69, 69], [100, 100]]
b = 100
print(knapsackProblem(a, b)) # 101

a = [[1, 2], [70, 70], [30, 30], [69, 69], [99, 100]]
b = 100
print(knapsackProblem(a, b)) # 100

a = [[1, 2], [70, 70], [30, 30], [69, 69], [100, 100]]
b = 0
print(knapsackProblem(a, b)) # 0

print("-----")

"""
    followup: output the indices of items as well
    very annoying implementation

    Time    O(NC)
    Space   O(NC)
"""
def knapsackProblem(items, capacity):
    ht = {}
    v, nums = dfs(items, 0, capacity, ht)
    return [v, sorted(nums)]

def dfs(items, i, cap, ht):
    if i == len(items):
        return [0, []]
    
    key = (i, cap)
    if key in ht:
        return ht[key]
    
    selected = 0
    selectedIndices = []
    if cap >= items[i][1]:
        sumFromBack, indicesFromBack = dfs(items, i+1, cap - items[i][1], ht)
        selected = sumFromBack + items[i][0]
        selectedIndices = indicesFromBack + [i]
	
    notSelected, notSelectedindices = dfs(items, i+1, cap, ht)
    
    res = 0
    resIndices = []
    
    if selected > notSelected:
        res = selected
        resIndices = selectedIndices
    else:
        res = notSelected
        resIndices = notSelectedindices
    
    ht[key] = [res, resIndices]
    return ht[key]

a = [[1, 2], [4, 3], [5, 6], [6, 7]]
b = 10
print(knapsackProblem(a, b)) # [10, [1, 3]]

a = [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [240, 40]
]
b = 200
print(knapsackProblem(a, b)) # [1500, [3, 12, 14]]

a = [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [255, 40]
]
b = 200
print(knapsackProblem(a, b)) # [1505, [7, 12, 14, 15]]

a = [[2, 1], [70, 70], [30, 30], [69, 69], [100, 100]]
b = 100
print(knapsackProblem(a, b)) # [101, [0, 2, 3]]

a = [[1, 2], [70, 70], [30, 30], [69, 69], [99, 100]]
b = 100
print(knapsackProblem(a, b)) # [100, [1, 2]]

a = [[1, 2], [70, 70], [30, 30], [69, 69], [100, 100]]
b = 0
print(knapsackProblem(a, b)) # [0, []]