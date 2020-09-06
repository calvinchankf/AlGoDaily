"""
    1st: brute force + hashtable

    Time    O(N)
    Space   O(N)
    24 ms, faster than 100.00% 
"""


class Solution(object):
    def modifyString(self, s):
        A = [x for x in s]
        n = len(A)
        res = []
        for i in range(n):
            c = A[i]
            if c == '?':
                banned = set()
                if i > 0:
                    banned.add(res[-1])
                if i+1 < n:
                    banned.add(A[i+1])
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j not in banned:
                        res.append(j)
                        break
            else:
                res.append(c)
        return ''.join(res)


s = Solution()

a = "?zs"
print(s.modifyString(a))

a = "ubv?w"
print(s.modifyString(a))

a = "j?qg??b"
print(s.modifyString(a))

a = "??yw?ipkj?"
print(s.modifyString(a))
