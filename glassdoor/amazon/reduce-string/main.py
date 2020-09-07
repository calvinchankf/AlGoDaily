"""
    https://leetcode.com/discuss/interview-question/406092/Amazon-or-Phone-Screen-or-Reduced-String
"""


def reduceString(s):
    order = {}
    ht = {}
    for i in range(len(s)):
        c = s[i]
        # record the first occurence of each character
        if c not in order:
            order[c] = i
        # count the occurence of each character
        if c not in ht:
            ht[c] = 1
        else:
            ht[c] += 1
    # sort by frequency(descending), order by ascending order
    freqs = []
    for key in ht:
        freqs.append((ht[key], key))

    def cmpter(a, b):
        if a[0] == b[0]:
            return order[a[1]] - order[b[1]]
        return b[0] - a[0]
    freqs.sort(cmp=cmpter)
    # construct the result
    res = ''
    for f, k in freqs:
        res += k
    return res


a = 'hello world'
print(reduceString(a))
