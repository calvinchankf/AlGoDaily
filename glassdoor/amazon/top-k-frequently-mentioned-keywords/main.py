from collections import Counter

"""
    Question:
    - https://leetcode.com/discuss/interview-question/542597/

    Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

    Notes:
    - The comparison of strings is case-insensitive.
    - Multiple occurances of a keyword in a review should be considred as a single mention.
    - If keywords are mentioned an equal number of times in reviews, sort alphabetically.

    Example 1:

    Input:
    k = 2
    keywords = ["anacell", "cetracular", "betacellular"]
    reviews = [
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
    ]

    Output:
    ["anacell", "betacellular"]

    Explanation:
    "anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
    Example 2:

    Input:
    k = 2
    keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
    "I love anacell Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular.",
    ]

    Output:
    ["betacellular", "anacell"]

    Explanation:
    "betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
    Related problems:

    https://leetcode.com/problems/top-k-frequent-words/
    https://leetcode.com/problems/top-k-frequent-elements/
"""


def topK(k, keywords, reviews):
    keywordSet = set(keywords)
    counter = Counter()
    for r in reviews:
        words = r.lower().split()
        # Multiple occurances of a keyword in a review should be considred as a single mention.
        seen = set()
        for w in words:
            if w in keywordSet:
                seen.add(w)
        for key in seen:
            counter[key] += 1

    freqs = []
    for key in counter:
        freqs.append((counter[key], key))

    def cmpter(a, b):
        if a[0] == b[0]:
            return -1 if a[1] < b[1] else 1
        return b[0] - a[0]
    freqs.sort(cmp=cmpter)

    res = []
    for i in range(min(k, len(freqs))):
        res.append(freqs[i][1])
    return res


"""
a = ['z', 'd', 'sd', 'hgh', 'fdf', 'bv']
def cmptr(a, b):
    return -1 if a < b else 1
a.sort(cmp=cmptr)
print(a) # ['bv', 'd', 'fdf', 'hgh', 'sd', 'z']
"""

a = 2
b = ["anacell", "cetracular", "betacellular"]
c = [
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
]
print(topK(a, b, c))

a = 2
b = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
c = [
    "I love anacell Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular.",
]
print(topK(a, b, c))

# a = 2
# b = ["anacell", "cetracular", "betacellular"]
# c = [
#     "I love anacell Best services; Best services provided by anacell",
#     "betacellular has great services",
#     "deltacellular provides much better services than betacellular",
#     "cetracular is worse than anacell",
#     "Betacellular is better than deltacellular.",
# ]
# print(topK(a, b, c))
