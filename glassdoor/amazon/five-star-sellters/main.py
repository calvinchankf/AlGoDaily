from typing import *
from heapq import *

"""
    https://leetcode.com/discuss/interview-question/933383/
    https://aonecode.com/amazon-online-assessment-five-star-sellers

    Third-party companies that sell their products on Amazon.com are able to analyze the customer reviews for their products in real time.
    Imagine that Amazon is creating a category called "five-star sellers"
    that will only display products sold by companies whose average percentage of five-star reviews per-product is at or above a certain threshold.
    Given the number of five-star and total reviews for each product a company sells,
    as well as the threshold percentage,
    what is the minimum number of additional fivestar reviews the company needs to become a five-star seller?

    For example, let's say there are 3 products (n = 3) where productRatings = [[4,4], [1,2], [3, 6]], and the percentage ratings Threshold = 77.
    The first number for each product in productRatings denotes the number of fivestar reviews, and the second denotes the number of total reviews.
    Here is how we can get the seller to reach the threshold with the minimum number of additional five-star reviews:

    Before we add more five-star reviews, the percentage for this seller is ((4 / 4) + (1/2) + (3/6))/3 = 66.66%
    If we add a five-star review to the second product, the percentage rises to ((4 / 4) + (2/3) +(3/6))/3 = 72.22%
    If we add another five-star review to the second product, the percentage rises to ((4 / 4) + (3/4) + (3/6))/3 = 75.00%
    If we add a five-star review to the third product, the percentage rises to ((4/4) + (3/4) + (4/7))/3 = 77.38%

    Input:
    reviews = [[4,4], [1,2], [3, 6]]
    ratingsThreshold = 77

    Output: 3
"""


def f(reviews, ratingsThreshold):
    """
        python3 for floating numbers

        Time    O(NlogN)
        Space   O(N)
    """
    n = len(reviews)
    threshold = n * ratingsThreshold

    # first thing is to check if the current ratings > threshold
    total = 0
    for fiveStar, overall in reviews:
        total += fiveStar/overall
    # print(total/n)
    if round(total * 100000) >= threshold * 1000:
        return 0

    # then we try to add a five star review for every product and then put the assumption into a maxheap
    pq = []
    for fiveStar, overall in reviews:
        if fiveStar <= overall:
            ratio = fiveStar/overall
            _ratio = (fiveStar + 1)/(overall + 1)
            _increase = _ratio - ratio
            heappush(pq, (-_increase, fiveStar+1, overall+1))

    # the increase from 1/2 to 2/3 is 50% -> 66.6% = +16.6%
    # the increase from 3/6 to 4/7 is 50% -> 57.1% = +7.1%
    # so we can use a maxheap to keep popping the most significant increase(of a review) and add it to total, then see if total > threshold
    count = 0
    while len(pq) > 0:
        increase, fiveStar, overall = heappop(pq)
        count += 1
        # since we use negative values to mimick using a maxheap, the new total = total - increase instead of total + increase
        total = total - increase
        # print(total/n)
        if round(total * 100000) >= threshold * 1000:  # x1000 to compare
            return count
        ratio = fiveStar/overall
        _ratio = (fiveStar + 1)/(overall + 1)
        _increase = _ratio - ratio
        heappush(pq, (-_increase, fiveStar+1, overall+1))

    return -1


a = [[4, 4], [1, 2], [3, 6]]
b = 77
print(f(a, b))

# corner case on floating numbers
a = [[1, 2], [3, 4], [4, 5]]
b = 80
print(f(a, b))
