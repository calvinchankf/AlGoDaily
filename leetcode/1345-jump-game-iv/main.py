"""
    1st: BFS + hashtable
    - similar to lc815, 1345
    - record all the indices for every number to jump in a dict
    - BFS
    - the crux: during BFS, to prevent stepping back, clear the dict for that number

    Time    O(N) -> O(N^2) depends on the number of indices having the same number
    Spave   O(N)
    4024 ms, faster than 5.11%
"""


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        cands = {}
        for i in range(n):
            x = arr[i]
            if x not in cands:
                cands[x] = []
            cands[x].insert(0, i)

        seen = set()
        q = [(0, 0)]
        while len(q) > 0:
            i, steps = q.pop(0)
            if i+1 == n:
                return steps
            if i < 0 or i == n:
                continue
            if i in seen:
                continue
            seen.add(i)
            # remove the cands after we consider them !!!
            for j in cands[arr[i]]:
                if j != i:
                    q.append((j, steps + 1))
            cands[arr[i]] = []
            # to the indices i-1, i+1
            q.append((i+1, steps + 1))
            q.append((i-1, steps + 1))

        return n - 1
