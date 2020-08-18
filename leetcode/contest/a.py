class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        m = {
            'N': (0,-1),
            'S': (0,1),
            'W': (-1,0),
            'E': (1,0),
        }
        hs = set()
        
        cur = [0, 0]
        key = (cur[0], cur[1])
        hs.add(key)
        for c in path:
            cur[0] += m[c][0]
            cur[1] += m[c][1]
            key = (cur[0], cur[1])
            if key in hs:
                return True
            hs.add(key)
        return False

s = Solution()

a = "NES"
print(s.isPathCrossing(a))

a = "NESWW"
print(s.isPathCrossing(a))