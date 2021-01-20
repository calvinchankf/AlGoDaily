"""
    We keep track of the revenue Facebook makes every day, 
    and we want to know on what days Facebook hits certain revenue milestones. 
    
    Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, 
    return an array containing the days on which Facebook reached every milestone.

    Signature
    int[] getMilestoneDays(int[] revenues, int[] milestones)
    
    Input
    revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.
    
    Output
    Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.
    
    Example
    revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    milestones = [100, 200, 500]
    output = [4, 6, 10]
    
    Explanation
    On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that FB has >= $200 of total revenue.
"""


def getMilestoneDays(revenues, milestones):
    pfs = 0
    pfss = []
    for r in revenues:
        pfs += r
        pfss.append(pfs)
    res = []
    for m in milestones:
        i = lowerBsearch(pfss, m)
        if i >= 0 and i < len(pfss):
            res.append(i + 1)
        else:
            res.append(-1)
    return res


def lowerBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left
