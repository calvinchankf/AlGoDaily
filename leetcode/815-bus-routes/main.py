from collections import defaultdict
"""
    0th: brute force BFS
    Time    O(N^N)
    Space   O(N)
    LTE
"""


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        connections = {}
        for route in routes:
            for stop in route:
                if stop not in connections:
                    connections[stop] = set(route)
                else:
                    for s in route:
                        connections[stop].add(s)
        q = [(S, 0)]
        seen = set([S])
        while len(q) > 0:
            node, steps = q.pop(0)
            # if node in seen:
            #     continue
            # seen.add(node)
            if node == T:
                return steps
            if node in connections:
                children = connections[node]
                for child in children:
                    if child not in seen:
                        seen.add(node)
                        q.append((child, steps + 1))
        return -1


s = Solution()

a = [[1, 2, 7], [3, 6, 7]]
b = 1
c = 6
print(s.numBusesToDestination(a, b, c))

a = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
b = 15
c = 12
print(s.numBusesToDestination(a, b, c))

print("----")

"""
    1st: optimized BFS
    - when we put nodes into the BFS queue, dont consider the current route for further exploration
    - we can use 2 hashtables to achieve that

    e.g.
    [[1,2,7],[3,6,7]]

    ht1 stores the relationshp of { routeId: stops }
    ht1 = {
        0: {1, 2, 7}, 
        1: {3, 6, 7}
    }

    ht2 stores the relationshp of { stopId: related routeIds }
    ht2 = {
        1: [0], 
        2: [0], 
        3: [1], 
        6: [1], 
        7: [0, 1]
    }

    Time    O(RS + RS^2) ???
    Space   O(N)
    1920 ms, faster than 9.62%
"""


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0

        # routeId: stops = { rid1: [stop1, stop2, stop3...], id2: [...], ... }
        routeSet = {}
        # stopId: related routeIds = { sid1: { rid1, rid2, rid3,...}, sid2: { rid1, rid2,..}... }
        connections = defaultdict(list)
        for i in range(len(routes)):
            route = routes[i]
            routeSet[i] = set(route)
            for stop in route:
                connections[stop].append(i)
        # BFS
        q = [(S, -1, 0)]
        seen = set()
        while len(q) > 0:
            node, curRoute, steps = q.pop(0)
            if node in seen:
                continue
            seen.add(node)
            if node == T:
                return steps
            # look for the related routes
            if node in connections:
                for rr in connections[node]:
                    if rr == curRoute:
                        continue
                    # put every bus stop into the queue from every related route
                    for stop in routeSet[rr]:
                        q.append((stop, rr, steps + 1))
        return -1


s = Solution()

a = [[1, 2, 7], [3, 6, 7]]
b = 1
c = 6
print(s.numBusesToDestination(a, b, c))

a = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
b = 15
c = 12
print(s.numBusesToDestination(a, b, c))

print("-----")

"""
    2nd: another BFS approach
    - instead of BFS through the bus stops, we BFS through the bus routes

    Time    O(RRS + RR) ???
    Space   O(N)
    2816 ms, faster than 5.02%
"""


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0

        starts = []
        # { rid1: [stop1, stop2, stop3...], id2: [..], ... }
        routeSet = {}
        for i in range(len(routes)):
            route = routes[i]
            routeSet[i] = set(route)
        # route connections { rid1: { rid2, rid3,...}, rid2: { rid1,..}... }
        connections = defaultdict(list)
        for i in routeSet:
            for stop in routeSet[i]:
                if stop == S:
                    starts.append(i)
                for j in routeSet:
                    if i == j:
                        continue
                    if stop in routeSet[j]:
                        connections[i].append(j)
        # BFS
        q = [(s, 1) for s in starts]
        seen = set()
        while len(q) > 0:
            route, steps = q.pop(0)
            if route in seen:
                continue
            seen.add(route)
            if T in routeSet[route]:
                return steps
            if route in connections:
                for rr in connections[route]:
                    q.append((rr, steps + 1))
        return -1


s = Solution()

a = [[1, 2, 7], [3, 6, 7]]
b = 1
c = 6
print(s.numBusesToDestination(a, b, c))

a = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
b = 15
c = 12
print(s.numBusesToDestination(a, b, c))

print("----")

"""
    3rd: similar to the 1st
    - similar to lc815, 1345
    - learned from others
    - but we clear each of the routes whenever after we put its stops in the BFS queue

    ht = {
        1: [0], 
        2: [0], 
        3: [1], 
        6: [1], 
        7: [0, 1]
    }

    - after we have seen stop1
        1. we put every stop from route0 in the queue 
        2. we clean up route0 <- so that whenever we route back to route0, we dont need to traverse again

    ref:
    - https://leetcode.com/problems/bus-routes/discuss/122771/C%2B%2BJavaPython-BFS-Solution


    Time    O(RS + RS)
    Space   O(RS)
    376 ms, faster than 84.10%
"""


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        # stopId: related routeIds = { sid1: { rid1, rid2, rid3,...}, sid2: { rid1, rid2,..}... }
        connections = defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                connections[j].add(i)
        # BFS
        q = [(S, 0)]
        seen = set()
        seen.add(S)
        while len(q) > 0:
            node, steps = q.pop(0)
            if node == T:
                return steps
            for routeId in connections[node]:
                for stop in routes[routeId]:
                    if stop not in seen:
                        seen.add(stop)
                        q.append((stop, steps + 1))
                # clean up routeId after it is considered
                routes[routeId] = []
        return -1


s = Solution()

a = [[1, 2, 7], [3, 6, 7]]
b = 1
c = 6
print(s.numBusesToDestination(a, b, c))

a = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
b = 15
c = 12
print(s.numBusesToDestination(a, b, c))
