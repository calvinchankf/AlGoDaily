"""
    0th: brute force BFS

    Time    O(2^N)
    LTE 100 / 190 test cases passed.
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        seen = set()
        q = [(sx, sy)]
        while len(q) > 0:
            x, y = q.pop(0)
            if x == tx and y == ty:
                return True
            if x > tx or y > ty:
                continue
            if (x, y) in seen:
                continue
            seen.add((x, y))

            q.append((x, x+y))
            q.append((x+y, y))
        return False


"""
    0th: math with -
    - learned from others
    - If we start from (sx, sy), it will be LTE to find (tx, ty)
    - If we start from (tx, ty), we can find only one path to go back to (sx, sy)

    see ./idea.png
    
    Time    O(N)
    LTE 150 / 190 test cases passed.
"""


class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty:
                return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False


"""
    1st: math with %
    - according to the approach above, we can speed up the process by using % instead
    - If we start from (sx, sy), it will be LTE to find (tx, ty)
    - If we start from (tx, ty), we can find only one path to go back to (sx, sy)
    
    see ./idea.png

    ref:
    - https://leetcode.com/problems/reaching-points/discuss/230588/Easy-to-understand-diagram-and-recursive-solution

    Time    O(log(min(TX, TY)))
    Space   O(1)
    24 ms, faster than 91.72% 
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty:
                return True
            if tx > ty:
                if ty == sy:
                    return (tx - sx) % ty == 0
                tx %= ty
            else:
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty %= tx
        return False
