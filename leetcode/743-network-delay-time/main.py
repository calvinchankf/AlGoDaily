import heapq


class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int

        It can be solved by BFS, but the main purpose of this attempt is to understand Dijkstra's Algorithm
        - Time  O(NlogN) logN due to the heap
        - Space O(N) result dict
        116ms beats 61.11%
        15may2019
        """
        # put times into a hashtable for lookup, time { from : [(to, weight)],... }
        connections = {}
        for u, v, w in times:
            if u in connections:
                connections[u].append((v, w))
            else:
                connections[u] = [(v, w)]

        # dijkstra's
        heap = [(0, K)]
        seen = {}
        while len(heap) > 0:
            weight, node = heapq.heappop(heap)

            if node in seen and weight >= seen[node]:
                continue
            seen[node] = weight

            if node in connections:
                cands = connections[node]
                for cand in cands:
                    heapq.heappush(heap, (weight+cand[1], cand[0]))

        # the max travel time is the result
        maxDelay = 0
        for i in range(1, N+1):
            if i not in seen:
                return -1
            if seen[i] > maxDelay:
                maxDelay = seen[i]
        return maxDelay


a = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
print(Solution().networkDelayTime(a, 4, 2))  # 2

a = [[2, 1, 1], [2, 3, 1], [1, 4, 3], [2, 4, 7]]
print(Solution().networkDelayTime(a, 4, 2))  # 4

a = [[1, 2, 3], [3, 4, 5]]
print(Solution().networkDelayTime(a, 4, 1))  # -1

"""
    here is the MST prim approach, it doesnt work because we can only calculate the min total cost to connect all the points
    BUT what we want is the max cost amongst the paths that from the start point(one path doesnt necessarily goes through all the points)
"""


class Solution(object):
    def networkDelayTime(self, times, N, K):
        visited = (N+1)*[False]
        pq = []
        res = 0
        for u, v, w in times:
            if u == K:
                heapq.heappush(pq, (w, u, v))
        visited[K] = True

        while len(pq) > 0:
            weight, start, end = heapq.heappop(pq)
            if visited[start] and visited[end]:
                continue
            else:
                visited[end] = True
                res += weight
                for u, v, w in times:
                    if u == end:
                        heapq.heappush(pq, (w, u, v))
        print(visited)
        return res
