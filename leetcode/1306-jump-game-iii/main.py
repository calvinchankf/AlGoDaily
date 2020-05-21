"""
    1st: bfs + hashtable
    
    Time    O(N)
    Space   O(N)
    252 ms, faster than 21.88%
"""


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        hs = set()
        q = [start]
        while len(q) > 0:
            idx = q.pop(0)
            if arr[idx] == 0:
                return True
            if idx in hs:
                continue
            hs.add(idx)
            if 0 <= idx - arr[idx] < len(arr):
                q.append(idx - arr[idx])
            if 0 <= idx + arr[idx] < len(arr):
                q.append(idx + arr[idx])
        return False
