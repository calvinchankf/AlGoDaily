from heapq import *

"""
    You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
    
    It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), 
    and as soon as you finish, the bag mysteriously refills. 
    
    If there were x pieces of candy in the bag at the beginning of the minute, 
    then after you've finished you'll find that floor(x/2) pieces are now inside.

    You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

    Signature
    int maxCandies(int[] arr, int K)

    Example 1
    
    Input
    arr = [2, 1, 7, 4, 2]
    k = 3
    
    Output = 14
    
    Explanation
    In the first minute you can eat 7 pieces of candy. That bag will refill with floor(7/2) = 3 pieces.
    In the second minute you can eat 4 pieces of candy from another bag. That bag will refill with floor(4/2) = 2 pieces.
    In the third minute you can eat the 3 pieces of candy that have appeared in the first bag that you ate.
    In total you can eat 7 + 4 + 3 = 14 pieces of candy.
"""


def maxCandies(arr, k):
    res = 0
    maxheap = []
    for x in arr:
        heappush(maxheap, -x)
    while k > 0:
        pop = -heappop(maxheap)
        res += pop
        half = pop//2
        heappush(maxheap, -half)
        k -= 1
    return res


a = [2, 1, 7, 4, 2]
b = 3
print(maxCandies(a, b))
