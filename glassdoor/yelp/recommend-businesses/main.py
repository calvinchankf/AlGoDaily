"""
    https://leetcode.com/discuss/interview-question/378040/Yelp-or-OA-2019-or-Recommend-Businesses

    Yelp can recommend businesses based on a distance you're willing to travel.

    Given a distance input and a connected acyclic graph of businesses with edges as distances, 
    return the list of names of businesses within the distance input.

    Input:
    starting business: a Business object to start from
    distance: int
    
    Output:
    list of str: A list of Business names that are within the given distance of the starting Business
    Distance is inclusive, meaning if a business is 5 away, then a distance input of 5 means that business IS reachable.

    The return value should NOT have the name of the starting business. 
    Therefore, if no businesses are within the given distance, return an empty list.

    The return value is NOT required to be sorted.

    Consider the following graph with distances where business A is the starting business.

           A
         /  \
      2 /    \ 4
       /      \
      B        C
       \
        \ 5
         \
          D

    findReachableBusinesses(A, 1); // should return an empty list
    findReachableBusinesses(A, 2); // should return ["B"]
    findReachableBusinesses(A, 3); // should also return ["B"]
    findReachableBusinesses(A, 4); // should return ["B", "C"]
    findReachableBusinesses(A, 7); // should return ["B", "C", "D"]
"""


class Business:
    def __init__(self, name):
        self.name = name
        self.nearbyBusinesses = {}


def findReachableBusinesses(start, distance):
    res = []
    q = [(start, 0)]
    while len(q) > 0:
        node, d = q.pop(0)
        if d <= distance and node != start:
            res.append(node.name)
        children = node.nearbyBusinesses
        for key in children:
            _d = children[key]
            q.append((key, d + _d))
    return res


A = Business('A')
B = Business('B')
C = Business('C')
D = Business('D')
A.nearbyBusinesses[B] = 2
A.nearbyBusinesses[C] = 4
B.nearbyBusinesses[D] = 5

print(findReachableBusinesses(A, 1))
print(findReachableBusinesses(A, 2))
print(findReachableBusinesses(A, 3))
print(findReachableBusinesses(A, 4))
print(findReachableBusinesses(A, 7))
