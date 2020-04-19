"""
    1st: intervals
    - similar to lc253

    Time    O(NlogN)
    Space   O(N)
    LTE 49 / 54 test cases passed.
"""


class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        prevOf = {
            'r': 'c',
            'o': 'r',
            'a': 'o',
            'k': 'a',
        }
        # [(start, end, string)....
        intvs = []
        for i in range(len(croakOfFrogs)):
            c = croakOfFrogs[i]
            if len(intvs) == 0:
                intvs.append([i, i, c])
            elif c == 'c':
                intvs.append([i, i, c])
            else:
                didBreak = False
                for j in range(len(intvs)):
                    lastChar = intvs[j][2][-1]
                    if prevOf[c] == lastChar:
                        intvs[j][1] = i + 1
                        intvs[j][2] += c
                        didBreak = True
                        break
                if didBreak == False:
                    return -1

        for i, j, s in intvs:
            if s != 'croak':
                return -1

        def cptr(a, b):
            if a[0] == b[0]:
                return a[1]-b[1]
            return a[0]-b[0]
        intvs = sorted(intvs, cmp=cptr)

        lasts = [intvs[0][1]]
        for i in range(1, len(intvs)):
            cur = intvs[i]
            found = False
            for j in range(len(lasts)):
                last = lasts[j]
                if last <= cur[0]:
                    lasts[j] = max(last, cur[1])
                    found = True
                    break
            if found == False:
                lasts.append(cur[1])
        return len(lasts)


s = Solution()

print(s.minNumberOfFrogs('croakcroak'))
print(s.minNumberOfFrogs('crcoakroak'))
print(s.minNumberOfFrogs('croakcrook'))
print(s.minNumberOfFrogs('croakcroa'))
