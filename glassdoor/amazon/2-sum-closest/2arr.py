"""
    Given 2 arrays of n flights, [id, travel distance], forwardRouteList and returnRouteList
    find the pair(s) in nums such that the sum is closest(<=) to a given number, target

    e.g.1
    maxTravelDist = 20
    forwardRouteList = [[1, 8], [2, 7], [3, 14]]
    returnRouteList = [[1, 5], [2, 10], [3, 14]]
    return [[3, 1]]

    e.g.2
    maxTravelDist = 20
    forwardRouteList = [[1, 8], [2, 15], [3, 9]]
    returnRouteList = [[1, 8], [2, 11], [3, 12]]
    return [[1, 3], [3, 2]]

    e.g.3
    maxTravelDist = 20
    forwardRouteList = [[1, 8], [2, 15], [3, 9], [4, 8]]
    returnRouteList = [[1, 8], [2, 11], [3, 12], [4, 12]]
    return [[1, 3], [3, 2], [1, 4], [4, 3], [4, 4]]
  
    Questions to ask:
    - will there be 2 or more pairs have the same sum? yes
    - on each array, will there be more than one item have the same travel distance? maybe
    - the result must contains 2 items? what if [1,2,10] and 10, should i just return 10?
    - will there be no result?
    - all numbers in nums > 0?
    - maxCap > 0?

    Time    O(mlogn) -> O(mn) because it might happen that there are duplicates travel distances in returnRoutes
    Space   O(n)

    ref:
    - https://leetcode.com/discuss/interview-question/373202
"""


def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    if maxTravelDist <= 0 or len(forwardRouteList) == 0 or len(returnRouteList) == 0:
        return []
    returnRouteList = sorted(returnRouteList)
    res = []
    best = 0
    for forward in forwardRouteList:
        returnIdx = bsearch(returnRouteList, maxTravelDist - forward[1])
        if returnIdx < 0:
            continue
        # iterate the returnRouteList if the curNum == prevNum
        while True:
            backward = returnRouteList[returnIdx]
            dist = forward[1] + backward[1]
            if dist > best:
                # reset the intermediate result
                best = dist
                res = [[forward[0], backward[0]]]
            elif dist == best:
                res.append([forward[0], backward[0]])
            if returnRouteList[returnIdx-1][1] != returnRouteList[returnIdx][1]:
                break
            returnIdx -= 1

    return res


# if no duplicate travel distance in returnRoutes, use this basic binary search
def bsearch(routes, target):
    left = 0
    right = len(routes) - 1
    while left <= right:
        mid = (left + right) // 2
        if routes[mid][1] < target:
            left = mid + 1
        elif routes[mid][1] > target:
            right = mid - 1
        else:
            return mid
    return right


a = 20
b = [[1, 8], [2, 7], [3, 14]]
c = [[1, 5], [2, 10], [3, 14]]
print(optimalUtilization(a, b, c))

a = 20
b = [[1, 8], [2, 15], [3, 9]]
c = [[1, 8], [2, 11], [3, 12]]
print(optimalUtilization(a, b, c))

a = 20
b = [[1, 8], [2, 15], [3, 9], [4, 8]]
c = [[1, 8], [2, 11], [3, 12], [4, 12], [5, 12]]
print(optimalUtilization(a, b, c))

# corner cases
a = -20
b = [[1, 8], [2, 7], [3, 14]]
c = [[1, 5], [2, 10], [3, 14]]
print(optimalUtilization(a, b, c))

a = 20
b = []
c = [[1, 5], [2, 10], [3, 14]]
print(optimalUtilization(a, b, c))

a = 20
b = [[1, 21], [2, 22], [3, 23]]
c = [[1, 24], [2, 25], [3, 26]]
print(optimalUtilization(a, b, c))

print("-----")

"""
    a = 20
    b = [[1, 8], [2, 15], [3, 9], [4, 8]]
    c = [[1, 8], [2, 11], [3, 12], [4, 12], [5, 12]]

    aId = 1 matches bIdx = 3, 4, 5
"""


def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    if maxTravelDist <= 0 or len(forwardRouteList) == 0 or len(returnRouteList) == 0:
        return []
    returnRouteList = sorted(returnRouteList)
    res = []
    best = 0
    for aId, aVal in forwardRouteList:
        firstIdx = lowerBsearch(returnRouteList, maxTravelDist - aVal)
        lastIdx = upperbsearch(returnRouteList, maxTravelDist - aVal)
        if firstIdx < 0 or firstIdx == len(returnRouteList) or lastIdx < 0 or lastIdx == len(returnRouteList):
            continue
        for i in range(firstIdx, lastIdx + 1):
            bId, bVal = returnRouteList[i]
            if aVal + bVal > best:
                res = [[aId, bId]]
                best = aVal + bVal
            elif aVal + bVal == best:
                res.append([aId, bId])
    return res


def lowerBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left


def upperbsearch(routes, target):
    left = 0
    right = len(routes)
    while left < right:
        mid = (left + right) // 2
        if target >= routes[mid][1]:
            left = mid + 1
        else:
            right = mid
    return left - 1


a = 20
b = [[1, 8], [2, 7], [3, 14]]
c = [[1, 5], [2, 10], [3, 14]]
print(optimalUtilization(a, b, c))

a = 20
b = [[1, 8], [2, 15], [3, 9]]
c = [[1, 8], [2, 11], [3, 12]]
print(optimalUtilization(a, b, c))

a = 20
b = [[1, 8], [2, 15], [3, 9], [4, 8]]
c = [[1, 8], [2, 11], [3, 12], [4, 12], [5, 12]]
print(optimalUtilization(a, b, c))

# corner cases
a = -20
b = [[1, 8], [2, 7], [3, 14]]
c = [[1, 5], [2, 10], [3, 14]]
print(optimalUtilization(a, b, c))

a = 20
b = []
c = [[1, 5], [2, 10], [3, 14]]
print(optimalUtilization(a, b, c))

a = 20
b = [[1, 21], [2, 22], [3, 23]]
c = [[1, 24], [2, 25], [3, 26]]
print(optimalUtilization(a, b, c))
