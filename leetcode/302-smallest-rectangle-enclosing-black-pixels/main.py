"""
    1st: BFS

    Time    O(RC)
    Space   O(1)
    536 ms, faster than 50.28%
"""


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        R, C = len(image), len(image[0])

        top = x
        bottom = x
        left = y
        right = y

        hs = set()
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)

            if i < 0 or i == R or j < 0 or j == C:
                continue

            if image[i][j] == '0':
                continue

            if (i, j) in hs:
                continue
            hs.add((i, j))

            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)

            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))

        return (bottom - top + 1) * (right - left + 1)
