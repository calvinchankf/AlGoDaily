"""
    1st: BFS

    Time    O(9999) there are at most 9999 representations 
    Space   O(9999)
    1404 ms, faster than 7.85%
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadendsSet = set(deadends)
        visited = set()
        q = [('0000', 0)]
        while len(q) > 0:
            node, steps = q.pop(0)
            if node in deadendsSet:
                continue
            if node in visited:
                continue
            visited.add(node)
            if node == target:
                return steps
            for i in range(len(node)):
                digit = int(node[i])
                inc = (digit+9) % 10
                q.append((node[:i] + str(inc) + node[i+1:], steps+1))
                dec = (digit+1) % 10
                q.append((node[:i] + str(dec) + node[i+1:], steps+1))
        return -1
