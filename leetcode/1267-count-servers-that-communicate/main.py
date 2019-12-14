from collections import defaultdict

"""
    1st: hashtable
    - put all the coordinates(the one) in rows(horizontals) and verticals(columns) hashtables
    - iterate the rows(horizontals) and verticals(columns) hashtables. If the length of a value >=2, add the coordinates into the result hashtable
    - the length of the result hashtable is the result

    Time    O(RC+R+C)
    Space   O(RC) at max
    504 ms, faster than 27.45%
"""


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        horizontals, verticals = defaultdict(list), defaultdict(list)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    horizontals[i].append((i, j))
                    verticals[j].append((i, j))
        resultSet = set()
        for key in horizontals:
            if len(horizontals[key]) >= 2:
                resultSet |= set(horizontals[key])
        for key in verticals:
            if len(verticals[key]) >= 2:
                resultSet |= set(verticals[key])
        return len(resultSet)
